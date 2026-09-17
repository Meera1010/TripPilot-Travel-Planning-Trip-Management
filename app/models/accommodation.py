from datetime import datetime
from app.models import db

class HotelBooking(db.Model):
    __tablename__ = 'hotel_bookings'

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'), nullable=False)
    hotel_name = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(255), nullable=True)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    check_in = db.Column(db.DateTime, nullable=False)
    check_out = db.Column(db.DateTime, nullable=False)
    room_type = db.Column(db.String(64), default='Deluxe Room')
    confirmation_code = db.Column(db.String(64), nullable=True)
    total_cost = db.Column(db.Float, default=0.0)
    currency = db.Column(db.String(3), default='USD')
    contact_phone = db.Column(db.String(32), nullable=True)
    notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        nights = (self.check_out - self.check_in).days if self.check_in and self.check_out else 1
        return {
            'id': self.id,
            'trip_id': self.trip_id,
            'hotel_name': self.hotel_name,
            'address': self.address,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'check_in': self.check_in.isoformat() if self.check_in else None,
            'check_out': self.check_out.isoformat() if self.check_out else None,
            'nights': max(1, nights),
            'room_type': self.room_type,
            'confirmation_code': self.confirmation_code,
            'total_cost': self.total_cost,
            'currency': self.currency,
            'contact_phone': self.contact_phone,
            'notes': self.notes
        }
