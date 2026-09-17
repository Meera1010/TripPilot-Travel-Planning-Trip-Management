from datetime import datetime
from app.models import db

class Trip(db.Model):
    __tablename__ = 'trips'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    primary_destination = db.Column(db.String(128), nullable=False)
    cover_image_url = db.Column(db.String(255), default='/static/img/default-trip.jpg')
    currency = db.Column(db.String(3), default='USD', nullable=False)
    total_budget = db.Column(db.Float, default=0.0)
    status = db.Column(db.String(32), default='planning')  # planning, confirmed, ongoing, completed, cancelled
    visibility = db.Column(db.String(16), default='private')  # private, shared, public
    invite_code = db.Column(db.String(32), unique=True, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    destinations = db.relationship('Destination', backref='trip', lazy=True, cascade='all, delete-orphan')
    co_travelers = db.relationship('TripCoTraveler', backref='trip', lazy=True, cascade='all, delete-orphan')
    itinerary_days = db.relationship('ItineraryDay', backref='trip', lazy=True, cascade='all, delete-orphan')
    expenses = db.relationship('Expense', backref='trip', lazy=True, cascade='all, delete-orphan')
    packing_lists = db.relationship('PackingList', backref='trip', lazy=True, cascade='all, delete-orphan')
    accommodations = db.relationship('HotelBooking', backref='trip', lazy=True, cascade='all, delete-orphan')
    transports = db.relationship('TransportTicket', backref='trip', lazy=True, cascade='all, delete-orphan')
    documents = db.relationship('TravelDocument', backref='trip', lazy=True, cascade='all, delete-orphan')
    journal_entries = db.relationship('JournalEntry', backref='trip', lazy=True, cascade='all, delete-orphan')

    def to_dict(self):
        duration_days = (self.end_date - self.start_date).days + 1 if self.start_date and self.end_date else 0
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'owner_id': self.owner_id,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'duration_days': duration_days,
            'primary_destination': self.primary_destination,
            'cover_image_url': self.cover_image_url,
            'currency': self.currency,
            'total_budget': self.total_budget,
            'status': self.status,
            'visibility': self.visibility,
            'invite_code': self.invite_code,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class Destination(db.Model):
    __tablename__ = 'destinations'

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    country = db.Column(db.String(64), nullable=False)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    arrival_date = db.Column(db.Date, nullable=True)
    departure_date = db.Column(db.Date, nullable=True)
    notes = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'trip_id': self.trip_id,
            'name': self.name,
            'country': self.country,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'arrival_date': self.arrival_date.isoformat() if self.arrival_date else None,
            'departure_date': self.departure_date.isoformat() if self.departure_date else None,
            'notes': self.notes
        }

class TripCoTraveler(db.Model):
    __tablename__ = 'trip_co_travelers'

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    email = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(32), default='editor')  # viewer, editor, admin
    status = db.Column(db.String(32), default='accepted')  # pending, accepted, declined
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'trip_id': self.trip_id,
            'user_id': self.user_id,
            'email': self.email,
            'name': self.name,
            'role': self.role,
            'status': self.status
        }
