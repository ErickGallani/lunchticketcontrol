""" Tests for meal resources """
import unittest
import json
from app import get_app, create_app, db


class MealTestCase(unittest.TestCase):
    """ Meal resources test case """
    def setUp(self):
        self.app = get_app(create_app)(config_name="testing")
        self.test_app = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.close()
            db.drop_all()

    def test_home_endpoint(self):
        """ Just testing the unit test setup """
        return_value = self.test_app.get('/')
        data_json = json.loads(return_value.data.decode("utf-8"))

        assert 'message' in data_json, \
                "return does not have 'message' property - %r" % data_json
        assert data_json["message"] == 'Home endpoint', \
                "return of end point does not match - %r" % data_json["message"]

if __name__ == '__main__':
    unittest.main()
