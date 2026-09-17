from datetime import datetime
from app.models import db

class TravelEvent(db.Model):
    __tablename__ = 'travel_events'

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    category = db.Column(db.String(32), default='flight')
    description = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'trip_id': self.trip_id,
            'title': self.title,
            'start_time': self.start_time.isoformat() if self.start_time else None,
            'end_time': self.end_time.isoformat() if self.end_time else None,
            'category': self.category,
            'description': self.description
        }

class ReminderNotification(db.Model):
    __tablename__ = 'reminder_notifications'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'), nullable=True)
    title = db.Column(db.String(128), nullable=False)
    message = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(32), default='info')  # info, warning, reminder, alert
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'trip_id': self.trip_id,
            'title': self.title,
            'message': self.message,
            'type': self.type,
            'is_read': self.is_read,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
