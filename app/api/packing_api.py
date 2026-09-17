from flask import Blueprint, request, jsonify
from app.models import db
from app.models.packing import PackingList, PackingItem
from app.services.packing_optimizer import PackingOptimizerService
from app.services.auth_service import AuthService

packing_api = Blueprint('packing_api', __name__)

@packing_api.route('/trip/<int:trip_id>', methods=['GET'])
def get_packing_lists(trip_id):
    user = AuthService.get_current_user()
    if not user:
        return jsonify({'error': 'Unauthorized'}), 401

    lists = PackingList.query.filter_by(trip_id=trip_id).all()
    return jsonify({'packing_lists': [l.to_dict() for l in lists]}), 200

@packing_api.route('/recommend', methods=['POST'])
def recommend_packing():
    data = request.get_json() or {}
    climate = data.get('climate', 'warm')
    duration = int(data.get('duration_days', 7))

    recs = PackingOptimizerService.generate_packing_recommendations(climate, duration)
    return jsonify({'recommendations': recs}), 200
