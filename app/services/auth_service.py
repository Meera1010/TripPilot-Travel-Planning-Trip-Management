from flask import session
from app.models import db
from app.models.user import User, Role, UserPreference, AuditLog

class AuthService:
    """User Authentication, Password Hashing & RBAC Manager."""

    @staticmethod
    def register_user(username, email, password, full_name, role='traveler'):
        """Register a new user with PBKDF2 password hashing."""
        if User.query.filter((User.username == username) | (User.email == email)).first():
            return None, "Username or Email already registered"

        user = User(
            username=username,
            email=email,
            full_name=full_name,
            role=role
        )
        user.set_password(password)

        # Create default preferences
        pref = UserPreference(theme='dark', temperature_unit='C', distance_unit='km')
        user.preferences = pref

        db.session.add(user)
        db.session.commit()

        AuthService.log_audit(user.id, 'REGISTER', 'user', user.id, 'User account registered')
        return user, None

    @staticmethod
    def authenticate_user(username_or_email, password):
        """Authenticate user by username/email and password."""
        user = User.query.filter(
            (User.username == username_or_email) | (User.email == username_or_email)
        ).first()

        if not user or not user.check_password(password):
            return None, "Invalid username or password"

        if not user.is_active:
            return None, "Account is disabled"

        session['user_id'] = user.id
        session['username'] = user.username
        session['role'] = user.role

        AuthService.log_audit(user.id, 'LOGIN', 'user', user.id, 'User logged in')
        return user, None

    @staticmethod
    def logout_user():
        """Destroy current user session."""
        user_id = session.get('user_id')
        if user_id:
            AuthService.log_audit(user_id, 'LOGOUT', 'user', user_id, 'User logged out')
        session.clear()
        return True

    @staticmethod
    def get_current_user():
        """Get currently logged-in user from session."""
        user_id = session.get('user_id')
        if not user_id:
            return None
        return User.query.get(user_id)

    @staticmethod
    def log_audit(user_id, action, resource_type, resource_id, details=''):
        """Write entry to security audit log."""
        try:
            log = AuditLog(
                user_id=user_id,
                action=action,
                resource_type=resource_type,
                resource_id=resource_id,
                details=details
            )
            db.session.add(log)
            db.session.commit()
        except Exception:
            db.session.rollback()
