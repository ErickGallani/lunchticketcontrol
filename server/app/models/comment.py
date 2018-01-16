from datetime import datetime
from app.database.database_config import db
from app.helpers.uuid_helper import generate_uuid


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.String(40), primary_key=True, default=generate_uuid)
    created_at = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.String(250), nullable=False)

    # relationship
    comment_id = db.Column(db.String(40), db.ForeignKey('comments.id'), nullable=True)
    meal_id = db.Column(db.String(40), db.ForeignKey('meals.id'), nullable=True)
    user_id = db.Column(db.String(40), db.ForeignKey('users.id'), nullable=False)

    def __init__(self, text):
        self.text = text
        self.created_at = datetime.now()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)

    def save_or_update(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
