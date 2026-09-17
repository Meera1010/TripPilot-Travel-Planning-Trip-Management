from flask import Blueprint, request, jsonify
from app.models import db
from app.models.transport import TransportTicket
from app.services.auth_service import AuthService

transport_api = Blueprint('transport_api', __name__)

@transport_api.route('/trip/<int:trip_id>', methods=['GET'])
def get_transport_tickets(trip_id):
    user = AuthService.get_current_user()
    if not user:
        return jsonify({'error': 'Unauthorized'}), 401

    tickets = TransportTicket.query.filter_by(trip_id=trip_id).order_by(TransportTicket.departure_time.asc()).all()
    return jsonify({'tickets': [t.to_dict() for t in tickets]}), 200
