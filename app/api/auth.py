from flask import Blueprint, request, jsonify, session
from app.services.auth_service import AuthService
from app.utils.validators import InputValidator
from app.utils.helpers import api_response
from app.utils.decorators import login_required_api
from app.models import db, UserPreference

auth_api = Blueprint('auth_api', __name__)

@auth_api.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    full_name = data.get('full_name')
    role = data.get('role', 'designer')
    brand_name = data.get('brand_name')

    if not InputValidator.validate_username(username):
        return api_response(False, message='Invalid username. 3-32 characters alphanumeric.', status_code=400)

    if not InputValidator.validate_email(email):
        return api_response(False, message='Invalid email address.', status_code=400)

    if not InputValidator.validate_password(password):
        return api_response(False, message='Password must be at least 6 characters.', status_code=400)

    user, error = AuthService.register_user(username, email, password, full_name or username, role, brand_name)
    if error:
        return api_response(False, message=error, status_code=400)

    # Auto-login after registration
    AuthService.authenticate(username, password)
    return api_response(True, data=user.to_dict(include_email=True), message='Registration successful', status_code=201)

@auth_api.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    username_or_email = data.get('username')
    password = data.get('password')

    if not username_or_email or not password:
        return api_response(False, message='Username and password are required', status_code=400)

    user, error = AuthService.authenticate(username_or_email, password)
    if error:
        return api_response(False, message=error, status_code=401)

    return api_response(True, data=user.to_dict(include_email=True), message='Login successful')

@auth_api.route('/logout', methods=['POST'])
def logout():
    AuthService.logout()
    return api_response(True, message='Logged out successfully')

@auth_api.route('/me', methods=['GET'])
def get_current_user():
    user = AuthService.get_current_user()
    if not user:
        return api_response(False, message='Not authenticated', status_code=401)

    data = user.to_dict(include_email=True)
    if user.preferences:
        data['preferences'] = user.preferences.to_dict()
    return api_response(True, data=data)

@auth_api.route('/preferences', methods=['PUT'])
@login_required_api
def update_preferences():
    user = AuthService.get_current_user()
    data = request.get_json() or {}

    pref = UserPreference.query.filter_by(user_id=user.id).first()
    if not pref:
        pref = UserPreference(user_id=user.id)
        db.session.add(pref)

    pref.theme = data.get('theme', pref.theme)
    pref.default_currency = data.get('default_currency', pref.default_currency)
    pref.measurement_unit = data.get('measurement_unit', pref.measurement_unit)
    pref.canvas_grid_size = int(data.get('canvas_grid_size', pref.canvas_grid_size))
    pref.snap_to_grid = bool(data.get('snap_to_grid', pref.snap_to_grid))

    db.session.commit()
    return api_response(True, data=pref.to_dict(), message='Preferences updated')
