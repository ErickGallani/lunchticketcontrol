from datetime import datetime
import flask
from marshmallow import Schema, fields
from sqlalchemy_utils import PasswordType, force_auto_coercion
from app.database.database_config import db
from app.helpers.uuid_helper import generate_uuid

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

    # ticket_id = db.Column(db.String, db.ForeignKey('tickets.id'), nullable=True)

    ticket = db.relationship("Ticket", uselist=False, back_populates="user")

    ticket_histories = db.relationship('TicketHistory', backref='user', lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.created_at = datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.get().all()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    created_at = fields.DateTime()
    username = fields.Str()
