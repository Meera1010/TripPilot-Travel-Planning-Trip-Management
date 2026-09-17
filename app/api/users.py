from flask import Blueprint, request
from app.models import db, User, Role
from app.utils.helpers import api_response, paginate_query
from app.utils.decorators import login_required_api, role_required_api

users_api = Blueprint('users_api', __name__)

@users_api.route('', methods=['GET'])
@login_required_api
def list_users():
    role_filter = request.args.get('role')
    page = int(request.args.get('page', 1))

    query = User.query
    if role_filter:
        query = query.filter_by(role=role_filter)

    data = paginate_query(query.order_by(User.created_at.desc()), page=page)
    return api_response(True, data=data)

@users_api.route('/<int:user_id>', methods=['GET'])
@login_required_api
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return api_response(False, message='User not found', status_code=404)
    return api_response(True, data=user.to_dict(include_email=True))

@users_api.route('/roles', methods=['GET'])
@login_required_api
def list_roles():
    roles = Role.query.all()
    return api_response(True, data=[r.to_dict() for r in roles])
