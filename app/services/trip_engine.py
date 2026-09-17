import secrets
from datetime import datetime, timedelta
from app.models import db
from app.models.trip import Trip, Destination, TripCoTraveler
from app.models.itinerary import ItineraryDay

class TripEngineService:
    """Trip Management, Route Composition & Invitation Engine."""

    @staticmethod
    def create_trip(owner_id, title, primary_destination, start_date_str, end_date_str, currency='USD', budget=0.0, description=''):
        """Create new trip and auto-generate day-by-day itinerary skeleton."""
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()

        if end_date < start_date:
            return None, "End date cannot be before start date"

        trip = Trip(
            title=title,
            description=description,
            owner_id=owner_id,
            start_date=start_date,
            end_date=end_date,
            primary_destination=primary_destination,
            currency=currency,
            total_budget=budget,
            invite_code=secrets.token_hex(8)
        )
        db.session.add(trip)
        db.session.flush()

        # Auto-create day itinerary records
        num_days = (end_date - start_date).days + 1
        for day_idx in range(num_days):
            current_date = start_date + timedelta(days=day_idx)
            day_rec = ItineraryDay(
                trip_id=trip.id,
                day_number=day_idx + 1,
                date=current_date,
                title=f"Day {day_idx + 1}: Exploring {primary_destination}"
            )
            db.session.add(day_rec)

        db.session.commit()
        return trip, None

    @staticmethod
    def calculate_trip_progress(trip):
        """Calculate trip completion percentage based on dates."""
        today = datetime.utcnow().date()
        if today < trip.start_date:
            return {'status': 'Upcoming', 'progress_pct': 0, 'days_until': (trip.start_date - today).days}
        elif today > trip.end_date:
            return {'status': 'Completed', 'progress_pct': 100, 'days_ago': (today - trip.end_date).days}
        else:
            total_days = (trip.end_date - trip.start_date).days + 1
            elapsed_days = (today - trip.start_date).days + 1
            pct = round((elapsed_days / float(total_days)) * 100, 1)
            return {'status': 'Ongoing', 'progress_pct': pct, 'current_day': elapsed_days}
