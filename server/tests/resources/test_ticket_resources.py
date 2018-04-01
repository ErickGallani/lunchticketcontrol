""" Tests for meal resources """
import unittest
import json
from datetime import datetime
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

    def tearDown(self):
        with self.app.app_context():
            db.session.close()
            db.drop_all()

    def test_get_tickets_from_empty_database(self):
        # arrange
        tickets_array_length = 0

        # act
        return_value = self.test_app.get('/api/tickets')
        data_json = json.loads(return_value.data.decode("utf-8"))

        # assert
        self.assertIsNotNone(data_json)
        self.assertIsNotNone(data_json['data'],
                             "return does not have 'tickets' (empty data) - %r" % data_json)
        self.assertEqual(tickets_array_length, len(data_json['data']))

    def test_get_tickets_passing_the_filter_date_in_query_string(self):
        # arrange
        tickets_array_length = 2
        ticket_datetime = datetime(2018, 3, 25)

        with self.app.app_context():
            load_test_data(ticket_datetime)

        # act
        return_value = self.test_app.get('/api/tickets?filter[date]=1521936000')
        data_json = json.loads(return_value.data.decode("utf-8"))

        # assert
        self.assertIsNotNone(data_json)
        self.assertIsNotNone(data_json['data'],
                             "return does not have 'tickets' (empty data) - %r" % data_json)
        self.assertEqual(tickets_array_length, len(data_json['data']))

    def test_get_tickets_passing_invalid_filter_date_str_instead_of_timestamp_in_query_string(self):
        # arrange
        tickets_array_length = 0
        ticket_datetime = datetime(2018, 3, 25)

        with self.app.app_context():
            load_test_data(ticket_datetime)

        # act
        return_value = self.test_app.get('/api/tickets?filter[date]=abcdef')
        data_json = json.loads(return_value.data.decode("utf-8"))

        # assert
        self.assertIsNotNone(data_json)
        self.assertIsNotNone(data_json['data'],
                             "return does not have 'tickets' (empty data) - %r" % data_json)
        self.assertEqual(tickets_array_length, len(data_json['data']))

def load_test_data(test_date):
    user = User('test123', 'abc123')
    user.save()
    user = User.query.all()[0]

    meal = Meal('Test meal', 'Meal desciption', test_date, b'009383615')
    meal.save()
    meal = Meal.query.all()[0]

    availability = Availability(test_date, meal.id)
    availability.save()
    availability = Availability.query.all()[0]

    ticket1 = Ticket(test_date, user.id, availability.id)
    ticket1.save()

    ticket2 = Ticket(test_date, user.id, availability.id)
    ticket2.save()

if __name__ == '__main__':
    unittest.main()
