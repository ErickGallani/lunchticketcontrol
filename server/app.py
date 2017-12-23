from setup import api, app

from resources.user import UserResource
from resources.ticket import TicketResource

UserResource.register(api)
TicketResource.register(api)

if __name__ == '__main__':
    from database.config import db

    db.init_app(app)
    app.run(host='127.0.0.1', port=5050, debug=True)
