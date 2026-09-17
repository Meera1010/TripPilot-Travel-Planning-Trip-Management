from datetime import datetime
from app.models import db

class TravelDocument(db.Model):
    __tablename__ = 'travel_documents'

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    type = db.Column(db.String(32), default='passport')  # passport, visa, insurance, flight_ticket, hotel_voucher, drivers_license
    document_number = db.Column(db.String(64), nullable=True)
    file_url = db.Column(db.String(255), nullable=True)
    notes = db.Column(db.Text, nullable=True)
    expiry_date = db.Column(db.Date, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'trip_id': self.trip_id,
            'user_id': self.user_id,
            'title': self.title,
            'type': self.type,
            'document_number': self.document_number,
            'file_url': self.file_url,
            'notes': self.notes,
            'expiry_date': self.expiry_date.isoformat() if self.expiry_date else None,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
