from datetime import datetime
from app.database.database_config import db
from app.helpers.uuid_helper import generate_uuid


class Ticket(db.Model):
    __tablename__ = 'tickets'

    id = db.Column(db.String(40), primary_key=True, default=generate_uuid)
    created_at = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.DateTime, nullable=False)

    availability_id = db.Column(db.String, db.ForeignKey('availabilities.id'), nullable=True)

    user_id = db.Column(db.String, db.ForeignKey('users.id'), nullable=True)
    user = db.relationship("User", back_populates="ticket")

    def __init__(self, time):
        self.time = time
        self.created_at = datetime.now()

    @classmethod
    def find_by_date(cls, date):
        return cls.query.filter_by(time=date)

    def save_or_update(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
