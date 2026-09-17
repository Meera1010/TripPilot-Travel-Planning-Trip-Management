import os
from app import create_app

app = create_app(os.environ.get('FLASK_ENV', 'development'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5050))
    host = os.environ.get('HOST', '127.0.0.1')
    app.run(host=host, port=port, debug=True)
