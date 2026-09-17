class CarbonCalculatorService:
    """Travel Transport CO2 Emission Estimator & Carbon Offset Engine."""

    EMISSION_FACTORS_KG_PER_KM = {
        'flight_short': 0.255,   # Short haul flight < 1500km
        'flight_long': 0.150,    # Long haul flight > 1500km
        'train_electric': 0.035, # High-speed electric rail (TGV/Eurostar/Shinkansen)
        'car_gasoline': 0.170,   # Average petrol car
        'bus_coach': 0.080       # Intercity coach bus
    }

    @staticmethod
    def calculate_emissions(transport_type='flight_short', distance_km=1000.0):
        """Calculate CO2 emissions in kilograms and offset cost in USD."""
        factor = CarbonCalculatorService.EMISSION_FACTORS_KG_PER_KM.get(transport_type, 0.150)
        co2_kg = round(distance_km * factor, 2)
        co2_tons = co2_kg / 1000.0
        offset_cost = round(co2_tons * 15.0, 2)  # $15 per ton carbon offset price

        return {
            'transport_type': transport_type,
            'distance_km': distance_km,
            'co2_emitted_kg': co2_kg,
            'co2_emitted_tons': round(co2_tons, 3),
            'recommended_offset_usd': max(1.0, offset_cost),
            'trees_to_plant': max(1, int(co2_kg / 20.0))
        }
