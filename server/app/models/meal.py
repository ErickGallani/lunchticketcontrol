from datetime import datetime
from app.database.database_config import db
from app.helpers.uuid_helper import generate_uuid


class Meal(db.Model):
    __tablename__ = 'meals'

    id = db.Column(db.String(40), primary_key=True, default=generate_uuid)
    created_at = db.Column(db.DateTime, nullable=False)
    picture = db.Column(db.LargeBinary, nullable=False)
    title = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String(250), nullable=False)

    def __init__(self, title, description, picture):
        self.title = title
        self.description = description
        self.picture = picture
        self.created_at = datetime.now()

    def save_or_update(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
