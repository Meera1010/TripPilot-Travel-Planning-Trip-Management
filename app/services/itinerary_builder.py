from app.models import db
from app.models.itinerary import ItineraryDay, ItineraryActivity

class ItineraryBuilderService:
    """Day-by-Day Timeline Builder & Schedule Conflict Detector."""

    @staticmethod
    def add_activity(day_id, title, category='sightseeing', start_time=None, end_time=None, location_name=None, lat=None, lng=None, cost=0.0, notes='', booking_ref=''):
        """Add an activity to an itinerary day timeline."""
        day = ItineraryDay.query.get(day_id)
        if not day:
            return None, "Itinerary day not found"

        order_index = len(day.activities) + 1
        activity = ItineraryActivity(
            day_id=day_id,
            title=title,
            category=category,
            start_time=start_time,
            end_time=end_time,
            location_name=location_name,
            latitude=lat,
            longitude=lng,
            estimated_cost=cost,
            notes=notes,
            booking_reference=booking_ref,
            order_index=order_index
        )
        db.session.add(activity)
        db.session.commit()
        return activity, None

    @staticmethod
    def detect_time_conflicts(day_activities):
        """Check for overlapping activity time windows."""
        conflicts = []
        timed_activities = [a for a in day_activities if a.start_time and a.end_time]
        
        for i in range(len(timed_activities)):
            for j in range(i + 1, len(timed_activities)):
                act1 = timed_activities[i]
                act2 = timed_activities[j]
                
                if (act1.start_time < act2.end_time) and (act2.start_time < act1.end_time):
                    conflicts.append({
                        'activity1_id': act1.id,
                        'activity1_title': act1.title,
                        'activity2_id': act2.id,
                        'activity2_title': act2.title,
                        'message': f"Overlap between '{act1.title}' ({act1.start_time}-{act1.end_time}) and '{act2.title}' ({act2.start_time}-{act2.end_time})"
                    })
        return conflicts
