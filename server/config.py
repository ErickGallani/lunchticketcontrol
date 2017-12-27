class Config(object):
    # Debug mode. This should be False in production mode
    DEBUG = False
    # Secret key to be used on authentoication using JWT
    SECRET_KEY = '3beeddd1e32bdadf478cdeba2c9222c36ca0b12a4808c7a35380e5a74ca4513f'
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_NAME = 'lunchticketapp'
    PASSWORD_SCHEMES = 'pbkdf2_sha512'


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
