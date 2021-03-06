""" This module is for aggregate all configs strategies """
class Config(object):
    """ Default config """
    # Application name
    APP_NAME = 'Lunch ticket'
    # Application host
    HOST = '127.0.0.1'
    # Application port
    PORT = 5050
    # Application protocol
    PROTOCOL = 'https'
    # Debug mode. This should be False in production mode
    DEBUG = False
    # Secret key to be used on authentoication using JWT
    SECRET_KEY = '3beeddd1e32bdadf478cdeba2c9222c36ca0b12a4808c7a35380e5a74ca4513f'
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_NAME = 'lunchticketapp'
    PASSWORD_SCHEMES = 'pbkdf2_sha512'
    SWAGGER_DOCS_URL = '/api/docs'
    API_SPEC_URL = '/api/swagger'
    API_VERSION = '1.0'

    @classmethod
    def get_swagger_api_url(cls):
        """
        Get full swagger api url.
        Eg.: http://127.0.0.1:5050/api/swagger.json
        """
        return "%s://%s:%s%s.json" % (cls.PROTOCOL, cls.HOST, cls.PORT, cls.API_SPEC_URL)


class ProductionConfig(Config):
    """ Production configuration """
    SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    """ Development configuration """
    DEBUG = True


class StagingConfig(Config):
    """ Staging configuration """
    DEBUG = True


class TestingConfig(Config):
    """ Test configuration """
    # in memory database
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    TESTING = True

APP_CONFIGS_TYPES = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}

def get_app_config(config_name):
    """
    Get the application configuration by configuration name
    :param config_name: Configuration name to retrieve the config class
    """
    return APP_CONFIGS_TYPES[config_name]
