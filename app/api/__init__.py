from flask import Blueprint

def register_api_blueprints(app):
    """Register all REST API blueprints with application instance."""
    from app.api.auth import auth_api
    from app.api.users import users_api
    from app.api.designs import designs_api
    from app.api.garments import garments_api
    from app.api.collections import collections_api
    from app.api.inventory import inventory_api
    from app.api.costing import costing_api
    from app.api.sizing import sizing_api
    from app.api.moodboards import moodboards_api
    from app.api.sketchbooks import sketchbooks_api
    from app.api.workflows import workflows_api
    from app.api.collaboration import collaboration_api
    from app.api.calendar import calendar_api
    from app.api.portfolios import portfolios_api
    from app.api.notifications import notifications_api
    from app.api.analytics import analytics_api
    from app.api.admin import admin_api

    app.register_blueprint(auth_api, url_prefix='/api/auth')
    app.register_blueprint(users_api, url_prefix='/api/users')
    app.register_blueprint(designs_api, url_prefix='/api/designs')
    app.register_blueprint(garments_api, url_prefix='/api/garments')
    app.register_blueprint(collections_api, url_prefix='/api/collections')
    app.register_blueprint(inventory_api, url_prefix='/api/inventory')
    app.register_blueprint(costing_api, url_prefix='/api/costing')
    app.register_blueprint(sizing_api, url_prefix='/api/sizing')
    app.register_blueprint(moodboards_api, url_prefix='/api/moodboards')
    app.register_blueprint(sketchbooks_api, url_prefix='/api/sketchbooks')
    app.register_blueprint(workflows_api, url_prefix='/api/workflows')
    app.register_blueprint(collaboration_api, url_prefix='/api/collaboration')
    app.register_blueprint(calendar_api, url_prefix='/api/calendar')
    app.register_blueprint(portfolios_api, url_prefix='/api/portfolios')
    app.register_blueprint(notifications_api, url_prefix='/api/notifications')
    app.register_blueprint(analytics_api, url_prefix='/api/analytics')
    app.register_blueprint(admin_api, url_prefix='/api/admin')
