from flask import Blueprint, request, jsonify
from app.services.weather_service import WeatherService

weather_api = Blueprint('weather_api', __name__)

@weather_api.route('/forecast', methods=['GET'])
def get_forecast():
    city = request.args.get('city', 'tokyo')
    forecast = WeatherService.get_destination_forecast(city)
    return jsonify({'city': city, 'forecast': forecast}), 200
