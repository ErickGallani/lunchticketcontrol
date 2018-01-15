import flask
from datetime import datetime
from app.database.database_config import db
from app.helpers.uuid_helper import generate_uuid
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

    ticket_id = db.Column(db.String, db.ForeignKey('tickets.id'), nullable=True)

    tickets_history = db.relationship('TicketHistory', backref='ticket_histories', lazy=True)

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
