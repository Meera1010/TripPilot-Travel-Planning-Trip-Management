from datetime import datetime
from app.models import db

class JournalEntry(db.Model):
    __tablename__ = 'journal_entries'

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text, nullable=False)
    entry_date = db.Column(db.Date, default=datetime.utcnow)
    location = db.Column(db.String(128), nullable=True)
    mood = db.Column(db.String(16), default='happy')  # happy, excited, relaxed, exhausted, amazed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    author = db.relationship('User')
    photos = db.relationship('TravelPhoto', backref='journal_entry', lazy=True, cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'trip_id': self.trip_id,
            'author_id': self.author_id,
            'author_name': self.author.full_name if self.author else 'Traveler',
            'title': self.title,
            'content': self.content,
            'entry_date': self.entry_date.isoformat() if self.entry_date else None,
            'location': self.location,
            'mood': self.mood,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'photos': [p.to_dict() for p in self.photos]
        }

class TravelPhoto(db.Model):
    __tablename__ = 'travel_photos'

    id = db.Column(db.Integer, primary_key=True)
    entry_id = db.Column(db.Integer, db.ForeignKey('journal_entries.id'), nullable=False)
    photo_url = db.Column(db.String(255), nullable=False)
    caption = db.Column(db.String(255), nullable=True)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'entry_id': self.entry_id,
            'photo_url': self.photo_url,
            'caption': self.caption,
            'uploaded_at': self.uploaded_at.isoformat() if self.uploaded_at else None
        }
