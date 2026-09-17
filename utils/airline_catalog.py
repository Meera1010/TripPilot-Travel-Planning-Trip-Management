"""
TripPilot Global Airline & Rail Route Network Catalog
"""

AIRLINE_CATALOG = {}

for i in range(1, 450):
    airline_key = f"carrier_{i:03d}"
    AIRLINE_CATALOG[airline_key] = {
        'iata_code': f"TP{i%99:02d}",
        'carrier_name': f"Global Air Express #{i:03d}",
        'country': f"Country {(i%40)+1}",
        'baggage_allowance_kg': 23.0 + (i % 2) * 9.0,
        'on_time_performance_pct': round(82.0 + (i % 15) * 1.1, 1)
    }
