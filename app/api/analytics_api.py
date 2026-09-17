from flask import Blueprint, jsonify
from app.services.analytics_service import AnalyticsService
from app.services.auth_service import AuthService

analytics_api = Blueprint('analytics_api', __name__)

@analytics_api.route('/dashboard', methods=['GET'])
def get_user_analytics():
    user = AuthService.get_current_user()
    if not user:
        return jsonify({'error': 'Unauthorized'}), 401

    stats = AnalyticsService.get_user_analytics(user.id)
    return jsonify({'analytics': stats}), 200
