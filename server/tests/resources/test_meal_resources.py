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

if __name__ == '__main__':
    unittest.main()
