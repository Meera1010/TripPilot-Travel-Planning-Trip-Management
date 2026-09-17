from datetime import datetime
from app.models import db

class ItineraryDay(db.Model):
    __tablename__ = 'itinerary_days'

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'), nullable=False)
    day_number = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    title = db.Column(db.String(128), nullable=True)
    summary = db.Column(db.Text, nullable=True)

    activities = db.relationship('ItineraryActivity', backref='itinerary_day', lazy=True, cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'trip_id': self.trip_id,
            'day_number': self.day_number,
            'date': self.date.isoformat() if self.date else None,
            'title': self.title,
            'summary': self.summary,
            'activities': [a.to_dict() for a in self.activities]
        }

class ItineraryActivity(db.Model):
    __tablename__ = 'itinerary_activities'

    id = db.Column(db.Integer, primary_key=True)
    day_id = db.Column(db.Integer, db.ForeignKey('itinerary_days.id'), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    category = db.Column(db.String(32), default='sightseeing')  # sightseeing, food, transport, hotel, shopping, relaxation
    start_time = db.Column(db.String(8), nullable=True)  # HH:MM
    end_time = db.Column(db.String(8), nullable=True)
    location_name = db.Column(db.String(255), nullable=True)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    estimated_cost = db.Column(db.Float, default=0.0)
    notes = db.Column(db.Text, nullable=True)
    booking_reference = db.Column(db.String(64), nullable=True)
    order_index = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            'id': self.id,
            'day_id': self.day_id,
            'title': self.title,
            'category': self.category,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'location_name': self.location_name,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'estimated_cost': self.estimated_cost,
            'notes': self.notes,
            'booking_reference': self.booking_reference,
            'order_index': self.order_index
        }
