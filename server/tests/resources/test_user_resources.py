""" Tests for User resources """
import unittest
import json
from app import get_app, create_app, db


class UserResourceTestCase(unittest.TestCase):
    """ User resources test case """
    def setUp(self):
        self.app = get_app(create_app)(config_name="testing")
        self.test_app = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.close()
            db.drop_all()

    def test_send_post_without_username(self):
        """ Test username validation """
        return_value = self.__user_post(password="123abc")
        assert b'This field cannot be blank.' in return_value.data

    def __user_post(self, **kwargs):
        # kwargs should be a key value pair for username and password
        # Eg. user_post(username='test', password='123')
        return self.app.post('/user',
                             data=dict(kwargs),
                             follow_redirects=True)


if __name__ == '__main__':
    unittest.main()
