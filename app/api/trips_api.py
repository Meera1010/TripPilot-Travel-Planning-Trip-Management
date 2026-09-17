from flask import Blueprint, request, jsonify, session
from app.models import db
from app.models.trip import Trip, Destination, TripCoTraveler
from app.services.trip_engine import TripEngineService
from app.services.auth_service import AuthService

trips_api = Blueprint('trips_api', __name__)

@trips_api.route('', methods=['GET'])
def list_trips():
    user = AuthService.get_current_user()
    if not user:
        return jsonify({'error': 'Unauthorized'}), 401

    status_filter = request.args.get('status')
    query = Trip.query.filter((Trip.owner_id == user.id) | (Trip.co_travelers.any(user_id=user.id)))

    if status_filter:
        query = query.filter(Trip.status == status_filter)

    trips = query.order_by(Trip.start_date.asc()).all()
    return jsonify({'trips': [t.to_dict() for t in trips]}), 200

@trips_api.route('', methods=['POST'])
def create_trip():
    user = AuthService.get_current_user()
    if not user:
        return jsonify({'error': 'Unauthorized'}), 401

    data = request.get_json() or {}
    title = data.get('title')
    primary_destination = data.get('primary_destination')
    start_date = data.get('start_date')
    end_date = data.get('end_date')

    if not title or not primary_destination or not start_date or not end_date:
        return jsonify({'error': 'Missing required trip fields'}), 400

    trip, error = TripEngineService.create_trip(
        owner_id=user.id,
        title=title,
        primary_destination=primary_destination,
        start_date_str=start_date,
        end_date_str=end_date,
        currency=data.get('currency', 'USD'),
        budget=float(data.get('total_budget', 0.0)),
        description=data.get('description', '')
    )

    if error:
        return jsonify({'error': error}), 400

    return jsonify({'message': 'Trip created successfully', 'trip': trip.to_dict()}), 201

@trips_api.route('/<int:trip_id>', methods=['GET'])
def get_trip(trip_id):
    user = AuthService.get_current_user()
    if not user:
        return jsonify({'error': 'Unauthorized'}), 401

    trip = Trip.query.get(trip_id)
    if not trip:
        return jsonify({'error': 'Trip not found'}), 404

    progress = TripEngineService.calculate_trip_progress(trip)
    res = trip.to_dict()
    res['progress'] = progress
    res['destinations'] = [d.to_dict() for d in trip.destinations]
    res['co_travelers'] = [c.to_dict() for c in trip.co_travelers]

    return jsonify({'trip': res}), 200
