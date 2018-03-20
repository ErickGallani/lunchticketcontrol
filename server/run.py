""" Runs the lunchticket webapi """
import os
from app import get_app, create_app

CONFIG_TYPE = os.getenv('APP_SETTINGS') or 'development'

APP = get_app(create_app)(CONFIG_TYPE)

if __name__ == '__main__':
    APP.run(host=APP.config.get('HOST'),
            port=APP.config.get('PORT'),
            ssl_context=('cert/localhost.crt',
                         'cert/localhost.key'))
