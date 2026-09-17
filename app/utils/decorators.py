from functools import wraps
from flask import session, jsonify, request, redirect, url_for
from app.models import User

def login_required_api(f):
    """API Decorator ensuring user is authenticated via session."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({'success': False, 'error': 'Authentication required. Please login.'}), 401
        return f(*args, **kwargs)
    return decorated_function

def role_required_api(allowed_roles):
    """API Decorator restricting endpoint access by role hierarchy."""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                return jsonify({'success': False, 'error': 'Authentication required.'}), 401
            
            user_role = session.get('role', 'designer')
            if user_role != 'admin' and user_role not in allowed_roles:
                return jsonify({'success': False, 'error': f'Permission denied. Required role: {allowed_roles}'}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def login_required_view(f):
    """Page View Decorator redirecting unauthenticated users to login."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth_views.login_page'))
        return f(*args, **kwargs)
    return decorated_function
