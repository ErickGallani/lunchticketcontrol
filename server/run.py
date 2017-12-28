import os
from app import get_app, create_app

config = os.getenv('APP_SETTINGS') or 'development'

app = get_app(create_app)(config)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050)
