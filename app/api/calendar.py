from flask import Blueprint, request
from datetime import datetime
from app.models import db, CalendarEvent, TaskItem
from app.services.auth_service import AuthService
from app.utils.helpers import api_response
from app.utils.decorators import login_required_api

calendar_api = Blueprint('calendar_api', __name__)

@calendar_api.route('/events', methods=['GET'])
def list_events():
    events = CalendarEvent.query.order_by(CalendarEvent.start_date.asc()).all()
    return api_response(True, data=[e.to_dict() for e in events])

@calendar_api.route('/events', methods=['POST'])
@login_required_api
def create_event():
    user = AuthService.get_current_user()
    data = request.get_json() or {}

    title = data.get('title')
    start_str = data.get('start_date')
    end_str = data.get('end_date')

    if not title or not start_str:
        return api_response(False, message='Title and start date are required', status_code=400)

    try:
        start_date = datetime.fromisoformat(start_str.replace('Z', '+00:00'))
        end_date = datetime.fromisoformat(end_str.replace('Z', '+00:00')) if end_str else start_date
    except Exception:
        start_date = datetime.utcnow()
        end_date = start_date

    event = CalendarEvent(
        title=title,
        description=data.get('description', ''),
        event_type=data.get('event_type', 'deadline'),
        start_date=start_date,
        end_date=end_date,
        collection_id=data.get('collection_id'),
        user_id=user.id,
        location=data.get('location', ''),
        color_tag=data.get('color_tag', '#ef233c')
    )
    db.session.add(event)
    db.session.commit()
    return api_response(True, data=event.to_dict(), message='Calendar event created', status_code=201)

@calendar_api.route('/tasks', methods=['GET'])
def list_tasks():
    tasks = TaskItem.query.order_by(TaskItem.due_date.asc()).all()
    return api_response(True, data=[t.to_dict() for t in tasks])
