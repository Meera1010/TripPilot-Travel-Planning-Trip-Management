from datetime import datetime, date, timedelta
from app.models import db
from app.models.user import User, Role, UserPreference, AuditLog
from app.models.trip import Trip, Destination, TripCoTraveler
from app.models.itinerary import ItineraryDay, ItineraryActivity
from app.models.expense import Expense, ExpenseSplit
from app.models.packing import PackingList, PackingItem
from app.models.accommodation import HotelBooking
from app.models.transport import TransportTicket
from app.models.journal import JournalEntry

def seed_database():
    """Populate SQLite database with realistic TripPilot travel SaaS seed data."""
    db.drop_all()
    db.create_all()

    print("Seeding TripPilot database...")

    # Roles
    admin_role = Role(name='admin', description='System Administrator', permissions='{"all": true}')
    traveler_role = Role(name='traveler', description='Standard Traveler', permissions='{"trips": true}')
    db.session.add_all([admin_role, traveler_role])
    db.session.flush()

    # Users
    admin = User(username='admin', email='admin@trippilot.io', full_name='System Admin', role='admin', role_id=admin_role.id)
    admin.set_password('Admin@123')
    admin.preferences = UserPreference(theme='dark', temperature_unit='C', distance_unit='km')

    alex = User(username='alex_traveler', email='alex@example.com', full_name='Alex Morgan', role='traveler', role_id=traveler_role.id)
    alex.set_password('Traveler@123')
    alex.preferences = UserPreference(theme='dark', temperature_unit='C', distance_unit='km')

    maya = User(username='maya_hikes', email='maya@example.com', full_name='Maya Lin', role='traveler', role_id=traveler_role.id)
    maya.set_password('Maya@123')
    maya.preferences = UserPreference(theme='dark', temperature_unit='C', distance_unit='km')

    db.session.add_all([admin, alex, maya])
    db.session.flush()

    # Trip 1: Tokyo Cherry Blossom Run
    trip1 = Trip(
        title='Tokyo Cherry Blossom Expedition',
        description='Spring 2026 trip across Tokyo, Kyoto, and Osaka to view Hanami cherry blossoms.',
        owner_id=alex.id,
        start_date=date(2026, 4, 1),
        end_date=date(2026, 4, 10),
        primary_destination='Tokyo, Japan',
        currency='USD',
        total_budget=3500.0,
        status='confirmed',
        invite_code='tokyo2026'
    )
    db.session.add(trip1)
    db.session.flush()

    # Co-traveler
    co1 = TripCoTraveler(trip_id=trip1.id, user_id=maya.id, email=maya.email, name=maya.full_name, role='editor', status='accepted')
    db.session.add(co1)

    # Destinations
    dest1 = Destination(trip_id=trip1.id, name='Tokyo', country='Japan', latitude=35.6762, longitude=139.6503, arrival_date=date(2026, 4, 1), departure_date=date(2026, 4, 5))
    dest2 = Destination(trip_id=trip1.id, name='Kyoto', country='Japan', latitude=35.0116, longitude=135.7681, arrival_date=date(2026, 4, 5), departure_date=date(2026, 4, 10))
    db.session.add_all([dest1, dest2])

    # Itinerary Days & Activities
    day1 = ItineraryDay(trip_id=trip1.id, day_number=1, date=date(2026, 4, 1), title='Arrival in Tokyo & Shinjuku Night Walk')
    act1 = ItineraryActivity(day_id=day1.id, title='Land at Narita International Airport', category='transport', start_time='14:00', end_time='16:00', location_name='Narita Airport', latitude=35.7720, longitude=140.3929, estimated_cost=30.0)
    act2 = ItineraryActivity(day_id=day1.id, title='Dinner at Omoide Yokocho', category='food', start_time='19:00', end_time='21:00', location_name='Shinjuku, Tokyo', latitude=35.6938, longitude=139.7004, estimated_cost=45.0)
    day1.activities.extend([act1, act2])
    db.session.add(day1)

    # Hotel & Transport
    hotel1 = HotelBooking(trip_id=trip1.id, hotel_name='Park Hyatt Tokyo', address='Shinjuku, Tokyo', latitude=35.6860, longitude=139.6917, check_in=datetime(2026, 4, 1, 15, 0), check_out=datetime(2026, 4, 5, 11, 0), total_cost=1200.0, confirmation_code='HYATT-8891')
    flight1 = TransportTicket(trip_id=trip1.id, type='flight', carrier_name='Japan Airlines', number_code='JL005', departure_location='JFK, New York', arrival_location='NRT, Tokyo', departure_time=datetime(2026, 3, 31, 11, 0), arrival_time=datetime(2026, 4, 1, 14, 0), cost=950.0)
    db.session.add_all([hotel1, flight1])

    # Expenses
    exp1 = Expense(trip_id=trip1.id, paid_by_id=alex.id, amount=240.0, currency='USD', category='food', title='Welcome Omakase Sushi Dinner', date=date(2026, 4, 1))
    split1 = ExpenseSplit(expense=exp1, user_id=alex.id, share_amount=120.0)
    split2 = ExpenseSplit(expense=exp1, user_id=maya.id, share_amount=120.0)
    exp1.splits.extend([split1, split2])
    db.session.add(exp1)

    # Journal
    journal1 = JournalEntry(trip_id=trip1.id, author_id=alex.id, title='Landed in Tokyo!', content='The flight was smooth. Stepping into Shinjuku at night felt like entering a cyberpunk world.', location='Shinjuku, Tokyo', mood='excited')
    db.session.add(journal1)

    # Audit log
    audit1 = AuditLog(user_id=alex.id, action='CREATE', resource_type='trip', resource_id=trip1.id, details='Created Tokyo Cherry Blossom trip')
    db.session.add(audit1)

    db.session.commit()
    print("Database seeding completed successfully!")

if __name__ == '__main__':
    seed_database()
