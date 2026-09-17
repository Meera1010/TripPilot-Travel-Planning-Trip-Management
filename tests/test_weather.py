from app.services.weather_service import WeatherService

def test_weather_forecast():
    forecast = WeatherService.get_destination_forecast('tokyo')
    assert len(forecast) == 5
    assert forecast[0]['day'] == 'Day 1'
    assert 'temp_celsius' in forecast[0]
