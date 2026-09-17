"""
TripPilot Global Hotels, Resorts & Boutique Accommodation Catalog
"""

HOTEL_CATALOG = {}

for i in range(1, 450):
    hotel_key = f"hotel_resort_{i:03d}"
    HOTEL_CATALOG[hotel_key] = {
        'id': hotel_key,
        'name': f"Grand Luxe Hotel #{i:03d}",
        'star_rating': 3 + (i % 3),
        'avg_nightly_rate_usd': round(80.0 + (i % 15) * 22.5, 2),
        'amenities': ['Free WiFi', 'Infinity Pool', 'Spa & Wellness', 'Airport Shuttle'],
        'cancellation_policy': 'Free cancellation up to 48 hours before check-in'
    }
