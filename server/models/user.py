from database.config import db
from database.types.guid import GUID 

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(GUID, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        return None

    @classmethod
    def find_by_id(cls, id):
        return None

    @classmethod
    def _find_by_(cls):
        return None