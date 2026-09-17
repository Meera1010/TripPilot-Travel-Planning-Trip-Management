from app.services.carbon_calculator import CarbonCalculatorService

def test_carbon_emission_calculation():
    res = CarbonCalculatorService.calculate_emissions('flight_short', 1000.0)
    assert res['co2_emitted_kg'] == 255.0
    assert res['recommended_offset_usd'] > 0
