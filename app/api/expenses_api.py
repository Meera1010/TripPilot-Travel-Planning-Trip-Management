from flask import Blueprint, request, jsonify
from app.models import db
from app.models.expense import Expense, ExpenseSplit
from app.services.expense_splitter import ExpenseSplitterService
from app.services.auth_service import AuthService

expenses_api = Blueprint('expenses_api', __name__)

@expenses_api.route('/trip/<int:trip_id>', methods=['GET'])
def get_trip_expenses(trip_id):
    user = AuthService.get_current_user()
    if not user:
        return jsonify({'error': 'Unauthorized'}), 401

    expenses = Expense.query.filter_by(trip_id=trip_id).order_by(Expense.date.desc()).all()
    user_balances = ExpenseSplitterService.calculate_group_balances(expenses)
    settlements = ExpenseSplitterService.simplify_debts(user_balances)

    return jsonify({
        'expenses': [e.to_dict() for e in expenses],
        'total_spent': sum(e.amount for e in expenses),
        'settlements': settlements
    }), 200

@expenses_api.route('', methods=['POST'])
def create_expense():
    user = AuthService.get_current_user()
    if not user:
        return jsonify({'error': 'Unauthorized'}), 401

    data = request.get_json() or {}
    trip_id = data.get('trip_id')
    title = data.get('title')
    amount = float(data.get('amount', 0.0))

    if not trip_id or not title or amount <= 0:
        return jsonify({'error': 'Invalid expense data'}), 400

    exp = Expense(
        trip_id=trip_id,
        paid_by_id=user.id,
        title=title,
        amount=amount,
        currency=data.get('currency', 'USD'),
        category=data.get('category', 'food'),
        notes=data.get('notes', '')
    )
    db.session.add(exp)
    db.session.commit()

    return jsonify({'message': 'Expense created', 'expense': exp.to_dict()}), 201
