from database.config import db
from database.helpers.uuid_helper import generate_uuid
import uuid

class Ticket(db.Model):
    __tablename__ = 'tickets'

    id = db.Column(db.String(40), primary_key=True, default=generate_uuid)
    created_at = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.DateTime, nullable=False)

    def __init__(self, time):
        self.time = time

    @classmethod
    def find_by_date(cls, date):
        return cls.query.filter_by(time=date).first()

    def save_or_update(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
