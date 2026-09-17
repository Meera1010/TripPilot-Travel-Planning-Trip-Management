import re

class InputValidator:
    """Validator and Sanitizer for REST API Request Payload Data."""

    @staticmethod
    def validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))

    @staticmethod
    def validate_username(username):
        pattern = r'^[a-zA-Z0-9_-]{3,32}$'
        return bool(re.match(pattern, username))

    @staticmethod
    def validate_password(password):
        # Minimum 6 characters
        return isinstance(password, str) and len(password) >= 6

    @staticmethod
    def validate_hex_color(color_hex):
        pattern = r'^#(?:[0-9a-fA-F]{3}){1,2}$'
        return bool(re.match(pattern, color_hex))

    @staticmethod
    def sanitize_string(text, max_length=255):
        if not text:
            return ''
        cleaned = str(text).strip()
        # Basic HTML tag stripping
        cleaned = re.sub(r'<[^>]*>', '', cleaned)
        return cleaned[:max_length]
