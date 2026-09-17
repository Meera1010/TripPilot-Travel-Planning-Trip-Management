from flask import Blueprint, request, jsonify
from app.models import db
from app.models.journal import JournalEntry
from app.services.auth_service import AuthService

journal_api = Blueprint('journal_api', __name__)

@journal_api.route('/trip/<int:trip_id>', methods=['GET'])
def get_journal_entries(trip_id):
    user = AuthService.get_current_user()
    if not user:
        return jsonify({'error': 'Unauthorized'}), 401

    entries = JournalEntry.query.filter_by(trip_id=trip_id).order_by(JournalEntry.entry_date.desc()).all()
    return jsonify({'entries': [e.to_dict() for e in entries]}), 200
