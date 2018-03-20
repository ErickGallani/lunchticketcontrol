""" Runs the lunchticket webapi """
import os
from app import get_app, create_app
from app.config import get_app_config

CONFIG_TYPE = os.getenv('APP_SETTINGS') or 'development'

APP = get_app(create_app)(CONFIG_TYPE)

CONFIG = get_app_config(CONFIG_TYPE)

if __name__ == '__main__':
    APP.run(host=CONFIG.HOST,
            port=CONFIG.PORT,
            ssl_context=('cert/localhost.crt',
                         'cert/localhost.key'))
