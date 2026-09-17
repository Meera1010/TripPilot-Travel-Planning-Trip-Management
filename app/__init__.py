import os
from flask import Flask
from app.config import config
from app.models import db

def create_app(config_name='default'):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config.get(config_name, config['default']))

    # Ensure instance directory exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    # Register API blueprints
    from app.api.auth_api import auth_api
    from app.api.trips_api import trips_api
    from app.api.itinerary_api import itinerary_api
    from app.api.expenses_api import expenses_api
    from app.api.packing_api import packing_api
    from app.api.transport_api import transport_api
    from app.api.hotels_api import hotels_api
    from app.api.journal_api import journal_api
    from app.api.weather_api import weather_api
    from app.api.analytics_api import analytics_api
    from app.api.admin_api import admin_api

    app.register_blueprint(auth_api, url_prefix='/api/auth')
    app.register_blueprint(trips_api, url_prefix='/api/trips')
    app.register_blueprint(itinerary_api, url_prefix='/api/itineraries')
    app.register_blueprint(expenses_api, url_prefix='/api/expenses')
    app.register_blueprint(packing_api, url_prefix='/api/packing')
    app.register_blueprint(transport_api, url_prefix='/api/transport')
    app.register_blueprint(hotels_api, url_prefix='/api/accommodations')
    app.register_blueprint(journal_api, url_prefix='/api/journal')
    app.register_blueprint(weather_api, url_prefix='/api/weather')
    app.register_blueprint(analytics_api, url_prefix='/api/analytics')
    app.register_blueprint(admin_api, url_prefix='/api/admin')

    # Register view routes
    from app.views.routes import main_bp
    app.register_blueprint(main_bp)

    # Database Seeding Command
    @app.cli.command('seed-db')
    def seed_db_command():
        from utils.seed_data import seed_database
        seed_database()

    # Set Content-Security-Policy and OWASP Security Headers
    @app.after_request
    def set_security_headers(response):
        csp_policy = (
            "default-src 'self'; "
            "script-src 'self' 'unsafe-inline' 'unsafe-eval' https://unpkg.com https://cdn.jsdelivr.net; "
            "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://unpkg.com; "
            "font-src 'self' https://fonts.gstatic.com; "
            "img-src 'self' data: https://*.tile.openstreetmap.org https://images.unsplash.com https://via.placeholder.com; "
            "connect-src 'self';"
        )
        response.headers['Content-Security-Policy'] = csp_policy
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        return response

    with app.app_context():
        db.create_all()
        from app.models.user import User
        if User.query.count() == 0:
            from utils.seed_data import seed_database
            seed_database()

    return app
