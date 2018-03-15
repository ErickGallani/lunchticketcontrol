""" Tests for meal resources """
import unittest
import json
from app import get_app, create_app, db


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

    def test_get_ticket(self):
        """ Just testing the unit test setup """
        return_value = self.test_app.get('/api/tickets')
        data_json = json.loads(return_value.data.decode("utf-8"))

        assert 'tickets' in data_json, \
                "return does not have 'tickets' property - %r" % data_json
        print(data_json["tickets"])

if __name__ == '__main__':
    unittest.main()
