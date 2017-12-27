import sys
import os
from setup import api, app
from flask_migrate import Migrate

sys.path.insert(0, os.path.dirname(__file__))

from database.config import db
from resources.user import UserResource
from resources.ticket import TicketResource

UserResource.add_to_api_resource(api)
TicketResource.add_to_api_resource(api)

db.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050, debug=True)