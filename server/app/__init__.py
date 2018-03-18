""" App bootstrap """
import logging
from flask import Flask
from flask_restful_swagger_2 import Api
from flask_swagger_ui import get_swaggerui_blueprint
from flask_jwt import JWT
from flask_cors import CORS
from raven.contrib.flask import Sentry
from app.auth.security import authenticate, identity
from app.resources.user import UserResource, UserWithIdResource, TicketHistoryResource
from app.resources.ticket import TicketResource
from app.resources.meal import MealResource, MealListResource
from app.resources.comment import CommentResource
from app.resources.home import HomeResource
from app.config import get_app_config
from app.database.database_config import db

SENTRY = Sentry()

APP_RETURN_ORDER = 0
API_RETURN_ORDER = 1
JWT_RETURN_ORDER = 2


def create_app(config_name):
    """ Instantiate a new app with JWT and Swagger """
    app = Flask(__name__)

    SENTRY.init_app(app, level=logging.ERROR)

    api_configs = get_app_config(config_name)

    app.config.from_object(api_configs)

    api = Api(app,
              api_version=api_configs.API_VERSION,
              api_spec_url=api_configs.API_SPEC_URL)

    jwt = JWT(app, authenticate, identity)  # /auth is the endpoint used by JWT

    # allow CORS for the swagger json endpoint to be able to use
    # swagger ui on endpoint /api/docs
    CORS(app, resources={r"%s.json" % api_configs.API_SPEC_URL: {"origins": "*"}})

    __add_resources(api)

    db.init_app(app)

    swaggerui_blueprint = get_swaggerui_blueprint(
        api_configs.SWAGGER_DOCS_URL,
        api_configs.get_swagger_api_url(),
        config={
            'app_name': api_configs.APP_NAME
        },
    )

    app.register_blueprint(swaggerui_blueprint,
                           url_prefix=api_configs.SWAGGER_DOCS_URL)

    return app, api, jwt


def __add_resources(api):
    """ Add resources to the api """
    # User resources
    UserResource.add_to_api_resource(api)
    UserWithIdResource.add_to_api_resource(api)

    # Ticket resources
    TicketResource.add_to_api_resource(api)
    TicketHistoryResource.add_to_api_resource(api)

    # Meal resources
    MealResource.add_to_api_resource(api)
    MealListResource.add_to_api_resource(api)

    # Comment resources
    CommentResource.add_to_api_resource(api)

    # Home resources
    HomeResource.add_to_api_resource(api)


def get_app(func):
    """ Get app object from the webapi object """
    def pick_app(*args, **kw):
        """ Wrapper to get the app from webapi object """
        return func(*args, **kw)[APP_RETURN_ORDER]
    return pick_app


def get_api(func):
    """ Get api object from the webapi object """
    def pick_api(*args, **kw):
        """ Wrapper to get the api from webapi object """
        return func(*args, **kw)[API_RETURN_ORDER]
    return pick_api


def get_jwt(func):
    """ Get jwt object from the webapi object """
    def pick_jwt(*args, **kw):
        """ Wrapper to get the jwt from webapi object """
        return func(*args, **kw)[JWT_RETURN_ORDER]
    return pick_jwt
