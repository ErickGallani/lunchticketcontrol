from datetime import datetime
from app.database.database_config import db
from app.helpers.uuid_helper import generate_uuid


class TicketHistory(db.Model):
    __tablename__ = 'ticket_histories'

    id = db.Column(db.String(40), primary_key=True, default=generate_uuid)
    created_at = db.Column(db.DateTime, nullable=False)

    user_id = db.Column(db.String, db.ForeignKey('users.id'), nullable=False)

    def __init__(self):
        self.created_at = datetime.now()

    def save_or_update(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
