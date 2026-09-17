from flask import Blueprint, request, jsonify, session
from app.services.auth_service import AuthService

auth_api = Blueprint('auth_api', __name__)

@auth_api.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    full_name = data.get('full_name', username)

    if not username or not email or not password:
        return jsonify({'error': 'Missing required fields'}), 400

    user, error = AuthService.register_user(username, email, password, full_name)
    if error:
        return jsonify({'error': error}), 400

    return jsonify({'message': 'Registration successful', 'user': user.to_dict()}), 201

@auth_api.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    username_or_email = data.get('username') or data.get('email')
    password = data.get('password')

    if not username_or_email or not password:
        return jsonify({'error': 'Missing username or password'}), 400

    user, error = AuthService.authenticate_user(username_or_email, password)
    if error:
        return jsonify({'error': error}), 401

    return jsonify({'message': 'Login successful', 'user': user.to_dict()}), 200

@auth_api.route('/logout', methods=['POST'])
def logout():
    AuthService.logout_user()
    return jsonify({'message': 'Logged out successfully'}), 200

@auth_api.route('/me', methods=['GET'])
def get_current_user():
    user = AuthService.get_current_user()
    if not user:
        return jsonify({'error': 'Not authenticated'}), 401
    return jsonify({'user': user.to_dict()}), 200
