import flask
import uuid
from database.config import db
from database.helpers.uuid_helper import generate_uuid
from datetime import datetime
from sqlalchemy_utils import PasswordType, force_auto_coercion

force_auto_coercion()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(40), primary_key=True, default=generate_uuid)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(
        PasswordType(
            # The returned dictionary is forwarded to the CryptContext
            onload=lambda **kwargs: dict(
                schemes=flask.current_app.config['PASSWORD_SCHEMES'],
                **kwargs
            ),
        ), unique=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.created_at = datetime.now()

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()