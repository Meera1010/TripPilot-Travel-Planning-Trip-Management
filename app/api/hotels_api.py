from flask import Blueprint, request, jsonify
from app.models import db
from app.models.accommodation import HotelBooking
from app.services.auth_service import AuthService

hotels_api = Blueprint('hotels_api', __name__)

@hotels_api.route('/trip/<int:trip_id>', methods=['GET'])
def get_hotel_bookings(trip_id):
    user = AuthService.get_current_user()
    if not user:
        return jsonify({'error': 'Unauthorized'}), 401

    bookings = HotelBooking.query.filter_by(trip_id=trip_id).order_by(HotelBooking.check_in.asc()).all()
    return jsonify({'bookings': [b.to_dict() for b in bookings]}), 200
