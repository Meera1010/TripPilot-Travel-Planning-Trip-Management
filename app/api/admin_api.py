from flask import Blueprint, jsonify
from app.models.user import User, AuditLog
from app.services.analytics_service import AnalyticsService
from app.services.auth_service import AuthService

admin_api = Blueprint('admin_api', __name__)

@admin_api.route('/stats', methods=['GET'])
def get_system_stats():
    user = AuthService.get_current_user()
    if not user or user.role != 'admin':
        return jsonify({'error': 'Admin access required'}), 403

    stats = AnalyticsService.get_admin_system_stats()
    return jsonify({'stats': stats}), 200

@admin_api.route('/audit-logs', methods=['GET'])
def get_audit_logs():
    user = AuthService.get_current_user()
    if not user or user.role != 'admin':
        return jsonify({'error': 'Admin access required'}), 403

    logs = AuditLog.query.order_by(AuditLog.timestamp.desc()).limit(100).all()
    return jsonify({'audit_logs': [l.to_dict() for l in logs]}), 200
