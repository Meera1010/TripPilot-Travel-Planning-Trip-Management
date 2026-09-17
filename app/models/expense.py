from datetime import datetime
from app.models import db

class Expense(db.Model):
    __tablename__ = 'expenses'

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'), nullable=False)
    paid_by_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(3), default='USD', nullable=False)
    category = db.Column(db.String(32), default='food')  # food, transport, hotel, activities, shopping, health, misc
    title = db.Column(db.String(128), nullable=False)
    date = db.Column(db.Date, default=datetime.utcnow)
    notes = db.Column(db.Text, nullable=True)
    receipt_url = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    paid_by = db.relationship('User', backref='paid_expenses')
    splits = db.relationship('ExpenseSplit', backref='expense', lazy=True, cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'trip_id': self.trip_id,
            'paid_by_id': self.paid_by_id,
            'paid_by_name': self.paid_by.full_name if self.paid_by else 'Unknown',
            'amount': self.amount,
            'currency': self.currency,
            'category': self.category,
            'title': self.title,
            'date': self.date.isoformat() if self.date else None,
            'notes': self.notes,
            'receipt_url': self.receipt_url,
            'splits': [s.to_dict() for s in self.splits]
        }

class ExpenseSplit(db.Model):
    __tablename__ = 'expense_splits'

    id = db.Column(db.Integer, primary_key=True)
    expense_id = db.Column(db.Integer, db.ForeignKey('expenses.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    share_amount = db.Column(db.Float, nullable=False)
    is_settled = db.Column(db.Boolean, default=False)

    user = db.relationship('User')

    def to_dict(self):
        return {
            'id': self.id,
            'expense_id': self.expense_id,
            'user_id': self.user_id,
            'user_name': self.user.full_name if self.user else 'Unknown',
            'share_amount': self.share_amount,
            'is_settled': self.is_settled
        }
