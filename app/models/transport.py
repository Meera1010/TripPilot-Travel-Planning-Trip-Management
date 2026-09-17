from datetime import datetime
from app.models import db

class TransportTicket(db.Model):
    __tablename__ = 'transport_tickets'

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'), nullable=False)
    type = db.Column(db.String(32), default='flight')  # flight, train, bus, rental_car, ferry
    carrier_name = db.Column(db.String(64), nullable=False)
    number_code = db.Column(db.String(32), nullable=True)  # Flight Number / Train Number
    departure_location = db.Column(db.String(128), nullable=False)
    arrival_location = db.Column(db.String(128), nullable=False)
    departure_time = db.Column(db.DateTime, nullable=False)
    arrival_time = db.Column(db.DateTime, nullable=False)
    seat_number = db.Column(db.String(16), nullable=True)
    confirmation_code = db.Column(db.String(64), nullable=True)
    cost = db.Column(db.Float, default=0.0)
    currency = db.Column(db.String(3), default='USD')
    notes = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'trip_id': self.trip_id,
            'type': self.type,
            'carrier_name': self.carrier_name,
            'number_code': self.number_code,
            'departure_location': self.departure_location,
            'arrival_location': self.arrival_location,
            'departure_time': self.departure_time.isoformat() if self.departure_time else None,
            'arrival_time': self.arrival_time.isoformat() if self.arrival_time else None,
            'seat_number': self.seat_number,
            'confirmation_code': self.confirmation_code,
            'cost': self.cost,
            'currency': self.currency,
            'notes': self.notes
        }
