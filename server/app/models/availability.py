from datetime import datetime
from app.database.database_config import db
from app.helpers.uuid_helper import generate_uuid


class Availability(db.Model):
    __tablename__ = 'availabilities'

    id = db.Column(db.String(40), primary_key=True, default=generate_uuid)
    created_at = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.DateTime, nullable=False)

    meal_id = db.Column(db.String, db.ForeignKey('meals.id'), nullable=False)

    tickets = db.relationship('Ticket', backref='tickets', lazy=True)

    def __init__(self):
        self.created_at = datetime.utcnow()

    def save_or_update(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
