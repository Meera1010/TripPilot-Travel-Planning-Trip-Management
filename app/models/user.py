from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import db

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    permissions = db.Column(db.Text, nullable=False, default='{}')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    users = db.relationship('User', backref='role_ref', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'permissions': self.permissions
        }

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    full_name = db.Column(db.String(128), nullable=False)
    avatar_url = db.Column(db.String(255), default='/static/img/default-avatar.png')
    bio = db.Column(db.Text, nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=True)
    role = db.Column(db.String(32), default='traveler', nullable=False)
    home_airport = db.Column(db.String(10), default='JFK')
    default_currency = db.Column(db.String(3), default='USD')
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    preferences = db.relationship('UserPreference', backref='user', uselist=False, cascade='all, delete-orphan')
    trips = db.relationship('Trip', backref='owner', lazy=True, cascade='all, delete-orphan')
    audit_logs = db.relationship('AuditLog', backref='user', lazy=True, cascade='all, delete-orphan')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'full_name': self.full_name,
            'avatar_url': self.avatar_url,
            'bio': self.bio,
            'role': self.role,
            'home_airport': self.home_airport,
            'default_currency': self.default_currency,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class UserPreference(db.Model):
    __tablename__ = 'user_preferences'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)
    theme = db.Column(db.String(16), default='dark')
    temperature_unit = db.Column(db.String(8), default='C') # C or F
    distance_unit = db.Column(db.String(8), default='km') # km or miles
    email_notifications = db.Column(db.Boolean, default=True)
    weather_alerts = db.Column(db.Boolean, default=True)
    budget_alerts = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            'theme': self.theme,
            'temperature_unit': self.temperature_unit,
            'distance_unit': self.distance_unit,
            'email_notifications': self.email_notifications,
            'weather_alerts': self.weather_alerts,
            'budget_alerts': self.budget_alerts
        }

class AuditLog(db.Model):
    __tablename__ = 'audit_logs'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    action = db.Column(db.String(64), nullable=False)
    resource_type = db.Column(db.String(64), nullable=False)
    resource_id = db.Column(db.Integer, nullable=True)
    ip_address = db.Column(db.String(45), nullable=True)
    details = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'action': self.action,
            'resource_type': self.resource_type,
            'resource_id': self.resource_id,
            'ip_address': self.ip_address,
            'details': self.details,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None
        }
