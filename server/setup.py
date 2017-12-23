from flask import Flask
from flask_restful_swagger_2 import Resource, Api
from flask_swagger_ui import get_swaggerui_blueprint
from flask_jwt import JWT
from auth.security import authenticate, identity

SWAGGER_URL = '/api/docs'
API_URL = 'http://127.0.0.1:5000/api/swagger.json'

app = Flask(__name__)
app.config.from_pyfile('settings.cfg', silent=True)
api = Api(app, api_version='1.0', api_spec_url='/api/swagger')

jwt = JWT(app, authenticate, identity) # /auth is the endpoint used by JWT

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Test application"
    },
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)