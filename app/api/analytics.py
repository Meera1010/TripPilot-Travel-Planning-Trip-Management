from flask import Blueprint
from app.services.analytics_service import AnalyticsService
from app.utils.helpers import api_response

analytics_api = Blueprint('analytics_api', __name__)

@analytics_api.route('/dashboard', methods=['GET'])
def get_dashboard_analytics():
    data = AnalyticsService.get_dashboard_metrics()
    return api_response(True, data=data)

@analytics_api.route('/snapshot', methods=['POST'])
def trigger_snapshot():
    snapshot = AnalyticsService.generate_daily_snapshot()
    return api_response(True, data=snapshot, message='Analytics snapshot created')
