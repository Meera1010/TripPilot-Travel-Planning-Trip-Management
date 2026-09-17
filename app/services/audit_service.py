from flask import request
from app.models import db, AuditLog

class AuditService:
    """Security and System Audit Logging Service."""

    @staticmethod
    def log_action(user_id, username, action, entity_type, entity_id=None, details=None):
        """Record an explicit audit entry in system log."""
        ip = request.remote_addr if request else '127.0.0.1'
        log = AuditLog(
            user_id=user_id,
            username=username or 'System',
            action=action,
            entity_type=entity_type,
            entity_id=str(entity_id) if entity_id else None,
            details=details or {},
            ip_address=ip
        )
        db.session.add(log)
        db.session.commit()
        return log

    @staticmethod
    def query_logs(action=None, entity_type=None, limit=50):
        """Retrieve filtered system audit logs for administrative review."""
        query = AuditLog.query
        if action:
            query = query.filter_by(action=action)
        if entity_type:
            query = query.filter_by(entity_type=entity_type)

        logs = query.order_by(AuditLog.timestamp.desc()).limit(limit).all()
        return [l.to_dict() for l in logs]
