class WeatherService:
    """Weather Forecast Engine & Climate Index Calculator."""

    CLIMATE_PRESETS = {
        'tokyo': {'temp_c': 18, 'condition': 'Sunny / Cherry Blossom Season', 'humidity_pct': 55, 'rain_prob_pct': 10, 'icon': '☀️'},
        'paris': {'temp_c': 22, 'condition': 'Partly Cloudy', 'humidity_pct': 60, 'rain_prob_pct': 20, 'icon': '⛅'},
        'bali': {'temp_c': 29, 'condition': 'Tropical Warm', 'humidity_pct': 80, 'rain_prob_pct': 40, 'icon': '🌴'},
        'manali': {'temp_c': 8, 'condition': 'Cool Mountain Breeze', 'humidity_pct': 45, 'rain_prob_pct': 15, 'icon': '🏔️'},
        'cairo': {'temp_c': 34, 'condition': 'Hot & Dry', 'humidity_pct': 25, 'rain_prob_pct': 0, 'icon': '🏜️'}
    }

    @staticmethod
    def get_destination_forecast(city_name='tokyo'):
        """Retrieve 5-day weather forecast for destination."""
        key = city_name.lower().replace(' ', '')
        base_weather = WeatherService.CLIMATE_PRESETS.get(key, WeatherService.CLIMATE_PRESETS['paris'])

        forecast = []
        for day in range(1, 6):
            temp_var = (day % 3) - 1
            forecast.append({
                'day': f"Day {day}",
                'temp_celsius': base_weather['temp_c'] + temp_var,
                'temp_fahrenheit': round((base_weather['temp_c'] + temp_var) * 1.8 + 32, 1),
                'condition': base_weather['condition'],
                'humidity_pct': base_weather['humidity_pct'],
                'rain_probability_pct': base_weather['rain_prob_pct'],
                'icon': base_weather['icon']
            })
        return forecast
