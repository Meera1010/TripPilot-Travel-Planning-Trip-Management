from flask import Blueprint, request
from app.models import db, AuditLog, User, Design, Collection, Fabric
from app.services.audit_service import AuditService
from app.utils.helpers import api_response, paginate_query
from app.utils.decorators import login_required_api, role_required_api

admin_api = Blueprint('admin_api', __name__)

@admin_api.route('/audit-logs', methods=['GET'])
@login_required_api
@role_required_api(['admin'])
def get_audit_logs():
    action = request.args.get('action')
    entity_type = request.args.get('entity_type')
    page = int(request.args.get('page', 1))

    query = AuditLog.query
    if action:
        query = query.filter_by(action=action)
    if entity_type:
        query = query.filter_by(entity_type=entity_type)

    data = paginate_query(query.order_by(AuditLog.timestamp.desc()), page=page)
    return api_response(True, data=data)

@admin_api.route('/system-status', methods=['GET'])
@login_required_api
@role_required_api(['admin'])
def get_system_status():
    status = {
        'database': 'Connected (SQLite)',
        'app_version': 'StyleForge SaaS 2.4.0-pro',
        'total_users': User.query.count(),
        'total_designs': Design.query.count(),
        'total_collections': Collection.query.count(),
        'total_fabrics': Fabric.query.count(),
        'audit_logs_recorded': AuditLog.query.count()
    }
    return api_response(True, data=status)
