from datetime import datetime
from app.models import db

class CarbonEmission(db.Model):
    __tablename__ = 'carbon_emissions'

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'), nullable=False)
    transport_mode = db.Column(db.String(32), nullable=False)  # flight_short, flight_long, train, car, bus
    distance_km = db.Column(db.Float, nullable=False)
    co2_kg = db.Column(db.Float, nullable=False)
    offset_cost_usd = db.Column(db.Float, default=0.0)

    def to_dict(self):
        return {
            'id': self.id,
            'trip_id': self.trip_id,
            'transport_mode': self.transport_mode,
            'distance_km': self.distance_km,
            'co2_kg': self.co2_kg,
            'offset_cost_usd': self.offset_cost_usd
        }

class TripSnapshot(db.Model):
    __tablename__ = 'trip_snapshots'

    id = db.Column(db.Integer, primary_key=True)
    snapshot_date = db.Column(db.Date, default=datetime.utcnow)
    active_trips_count = db.Column(db.Integer, default=0)
    total_users_count = db.Column(db.Integer, default=0)
    total_expenses_usd = db.Column(db.Float, default=0.0)
    total_destinations_count = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            'id': self.id,
            'snapshot_date': self.snapshot_date.isoformat() if self.snapshot_date else None,
            'active_trips_count': self.active_trips_count,
            'total_users_count': self.total_users_count,
            'total_expenses_usd': self.total_expenses_usd,
            'total_destinations_count': self.total_destinations_count
        }
