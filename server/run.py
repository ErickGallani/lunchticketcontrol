""" Runs the lunchticket webapi """
import os
from app import get_app, create_app

CONFIG = os.getenv('APP_SETTINGS') or 'development'

APP = get_app(create_app)(CONFIG)

if __name__ == '__main__':
    APP.run(host='127.0.0.1', port=5050)
