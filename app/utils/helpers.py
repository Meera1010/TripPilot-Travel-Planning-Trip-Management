import re
from flask import jsonify

def api_response(success=True, data=None, message=None, status_code=200):
    """Standardized API JSON response formatter."""
    payload = {'success': success}
    if data is not None:
        payload['data'] = data
    if message:
        payload['message' if success else 'error'] = message
    return jsonify(payload), status_code

def slugify(text):
    """Convert raw title to URL-friendly unique slug."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    text = re.sub(r'^-+|-+$', '', text)
    return text or 'untitled-design'

def paginate_query(query, page=1, per_page=12):
    """Paginate SQLAlchemy query and return formatted pagination metadata."""
    paginated = query.paginate(page=page, per_page=per_page, error_out=False)
    return {
        'items': [item.to_dict() for item in paginated.items],
        'total': paginated.total,
        'pages': paginated.pages,
        'current_page': paginated.page,
        'has_next': paginated.has_next,
        'has_prev': paginated.has_prev
    }
