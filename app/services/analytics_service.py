from app.models import db
from app.models.trip import Trip
from app.models.expense import Expense
from app.models.user import User

class AnalyticsService:
    """Trip Analytics & Spend Breakdown Aggregator."""

    @staticmethod
    def get_user_analytics(user_id):
        """Aggregate trip statistics, expenses, and category breakdowns for user."""
        user_trips = Trip.query.filter_by(owner_id=user_id).all()
        trip_ids = [t.id for t in user_trips]

        total_trips = len(user_trips)
        completed_trips = len([t for t in user_trips if t.status == 'completed'])
        upcoming_trips = len([t for t in user_trips if t.status == 'planning'])

        expenses = Expense.query.filter(Expense.trip_id.in_(trip_ids)).all() if trip_ids else []
        total_spent = sum(e.amount for e in expenses)

        category_breakdown = {}
        for e in expenses:
            category_breakdown[e.category] = category_breakdown.get(e.category, 0.0) + e.amount

        return {
            'total_trips': total_trips,
            'completed_trips': completed_trips,
            'upcoming_trips': upcoming_trips,
            'total_spent_usd': round(total_spent, 2),
            'category_breakdown': {k: round(v, 2) for k, v in category_breakdown.items()}
        }

    @staticmethod
    def get_admin_system_stats():
        """Retrieve system-wide analytics for admin portal."""
        total_users = User.query.count()
        total_trips = Trip.query.count()
        total_expenses = db.session.query(db.func.sum(Expense.amount)).scalar() or 0.0

        return {
            'total_registered_users': total_users,
            'total_created_trips': total_trips,
            'total_expenses_logged_usd': round(total_expenses, 2)
        }
