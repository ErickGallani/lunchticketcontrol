from datetime import datetime
from marshmallow import Schema, fields
from app.database.database_config import db
from app.helpers.uuid_helper import generate_uuid
from app.models.user import UserSchema

class Ticket(db.Model):
    __tablename__ = 'tickets'

    id = db.Column(db.String(40), primary_key=True, default=generate_uuid)
    created_at = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.DateTime, nullable=False)

    availability_id = db.Column(db.String, db.ForeignKey('availabilities.id'), nullable=True)

    user_id = db.Column(db.String, db.ForeignKey('users.id'), nullable=True)
    user = db.relationship("User", back_populates="ticket")

    def __init__(self, time, user_id, availability_id):
        self.time = time
        self.user_id = user_id
        self.availability_id = availability_id
        self.created_at = datetime.utcnow()

    @classmethod
    def find_by_date(cls, date):
        return cls.query.filter_by(time=date).all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class TicketSchema(Schema):
    id = fields.Str(dump_only=True)
    created_at = fields.DateTime()
    time = fields.DateTime()
    availability_id = fields.Str()
    user_id = fields.Str()

    user = fields.Nested(UserSchema)
