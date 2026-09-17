from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from app.models.user import User, Role, UserPreference, AuditLog
from app.models.trip import Trip, Destination, TripCoTraveler
from app.models.itinerary import ItineraryDay, ItineraryActivity
from app.models.accommodation import HotelBooking
from app.models.transport import TransportTicket
from app.models.expense import Expense, ExpenseSplit
from app.models.packing import PackingList, PackingItem
from app.models.document import TravelDocument
from app.models.journal import JournalEntry, TravelPhoto
from app.models.calendar import TravelEvent, ReminderNotification
from app.models.analytics import CarbonEmission, TripSnapshot

__all__ = [
    'db',
    'User', 'Role', 'UserPreference', 'AuditLog',
    'Trip', 'Destination', 'TripCoTraveler',
    'ItineraryDay', 'ItineraryActivity',
    'HotelBooking',
    'TransportTicket',
    'Expense', 'ExpenseSplit',
    'PackingList', 'PackingItem',
    'TravelDocument',
    'JournalEntry', 'TravelPhoto',
    'TravelEvent', 'ReminderNotification',
    'CarbonEmission', 'TripSnapshot'
]
