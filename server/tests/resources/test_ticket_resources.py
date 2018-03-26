""" Tests for meal resources """
import unittest
import json
from datetime import date
from app import get_app, create_app, db
from app.models.ticket import Ticket
from app.models.user import User
from app.models.meal import Meal
from app.models.availability import Availability

class TicketTestCase(unittest.TestCase):
    """ Ticket resources test case """
    def setUp(self):
        self.app = get_app(create_app)(config_name="testing")
        self.test_app = self.app.test_client()

        with self.app.app_context():
            db.create_all()
            load_test_data()

    def tearDown(self):
        with self.app.app_context():
            db.session.close()
            db.drop_all()

    def test_get_ticket(self):
        """ Just testing the unit test setup """
        return_value = self.test_app.get('/api/tickets')
        data_json = json.loads(return_value.data.decode("utf-8"))

        assert 'data' in data_json, \
                "return does not have 'tickets' (empty data) - %r" % data_json

        self.assertEqual(2, len(data_json['data']))

def load_test_data():
    ticket_date = date(2018, 3, 25)

    user = User('test123', 'abc123')
    user.save()
    user = User.query.all()[0]

    meal = Meal('Test meal', 'Meal desciption', ticket_date, b'009383615')
    meal.save()
    meal = Meal.query.all()[0]

    availability = Availability(ticket_date, meal.id)
    availability.save()
    availability = Availability.query.all()[0]

    ticket1 = Ticket(ticket_date, user.id, availability.id)
    ticket1.save()

    ticket2 = Ticket(ticket_date, user.id, availability.id)
    ticket2.save()

if __name__ == '__main__':
    unittest.main()
