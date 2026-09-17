from flask import Blueprint, request, jsonify
from app.models import db
from app.models.itinerary import ItineraryDay, ItineraryActivity
from app.services.itinerary_builder import ItineraryBuilderService
from app.services.auth_service import AuthService

itinerary_api = Blueprint('itinerary_api', __name__)

@itinerary_api.route('/trip/<int:trip_id>', methods=['GET'])
def get_trip_itinerary(trip_id):
    user = AuthService.get_current_user()
    if not user:
        return jsonify({'error': 'Unauthorized'}), 401

    days = ItineraryDay.query.filter_by(trip_id=trip_id).order_by(ItineraryDay.day_number.asc()).all()
    return jsonify({'days': [d.to_dict() for d in days]}), 200

@itinerary_api.route('/activities', methods=['POST'])
def add_activity():
    user = AuthService.get_current_user()
    if not user:
        return jsonify({'error': 'Unauthorized'}), 401

    data = request.get_json() or {}
    day_id = data.get('day_id')
    title = data.get('title')

    if not day_id or not title:
        return jsonify({'error': 'Missing required fields'}), 400

    activity, error = ItineraryBuilderService.add_activity(
        day_id=day_id,
        title=title,
        category=data.get('category', 'sightseeing'),
        start_time=data.get('start_time'),
        end_time=data.get('end_time'),
        location_name=data.get('location_name'),
        lat=data.get('latitude'),
        lng=data.get('longitude'),
        cost=float(data.get('estimated_cost', 0.0)),
        notes=data.get('notes', ''),
        booking_ref=data.get('booking_reference', '')
    )

    if error:
        return jsonify({'error': error}), 400

    return jsonify({'message': 'Activity added', 'activity': activity.to_dict()}), 201
