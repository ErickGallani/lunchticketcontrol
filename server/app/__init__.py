from flask import Flask
from flask_restful_swagger_2 import Api
from flask_swagger_ui import get_swaggerui_blueprint
from flask_jwt import JWT
from app.auth.security import authenticate, identity
from app.resources.user import UserResource
from app.resources.ticket import TicketResource
from app.config import app_config
from app.database.database_config import db

SWAGGER_URL = '/api/docs'
API_URL = 'http://127.0.0.1:5050/api/swagger.json'


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    api = Api(app, api_version='1.0', api_spec_url='/api/swagger')

    jwt = JWT(app, authenticate, identity)  # /auth is the endpoint used by JWT

    UserResource.add_to_api_resource(api)
    TicketResource.add_to_api_resource(api)

    db.init_app(app)

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Lunch ticket application"
        },
    )

    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    return app, api, jwt


def get_app(func):
    def pick_app(*args, **kw):
        return func(*args, **kw)[0]
    return pick_app


def get_api(func):
    def pick_api(*args, **kw):
        return func(*args, **kw)[1]
    return pick_api


def get_jwt(func):
    def pick_jwt(*args, **kw):
        return func(*args, **kw)[2]
    return pick_jwt
