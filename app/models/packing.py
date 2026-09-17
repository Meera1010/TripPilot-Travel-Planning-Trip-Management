from datetime import datetime
from app.models import db

class PackingList(db.Model):
    __tablename__ = 'packing_lists'

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    category = db.Column(db.String(32), default='general')  # clothes, electronics, toilet, documents, beach, winter

    items = db.relationship('PackingItem', backref='packing_list', lazy=True, cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'trip_id': self.trip_id,
            'name': self.name,
            'category': self.category,
            'items': [i.to_dict() for i in self.items]
        }

class PackingItem(db.Model):
    __tablename__ = 'packing_items'

    id = db.Column(db.Integer, primary_key=True)
    list_id = db.Column(db.Integer, db.ForeignKey('packing_lists.id'), nullable=False)
    item_name = db.Column(db.String(128), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    is_packed = db.Column(db.Boolean, default=False)
    weight_grams = db.Column(db.Float, default=0.0)

    def to_dict(self):
        return {
            'id': self.id,
            'list_id': self.list_id,
            'item_name': self.item_name,
            'quantity': self.quantity,
            'is_packed': self.is_packed,
            'weight_grams': self.weight_grams
        }
