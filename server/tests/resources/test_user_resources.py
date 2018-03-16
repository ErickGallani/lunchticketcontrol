""" Tests for User resources """
import unittest
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

        assert b'This field cannot be blank' in return_value.data
        assert b'username' in return_value.data

    def test_send_post_without_password(self):
        """ Test password validation """
        return_value = self.__user_post(username="test_username")

        assert b'This field cannot be blank' in return_value.data
        assert b'password' in return_value.data

    def test_send_post_with_username_and_password(self):
        """ Test insert user passing username and password with success"""
        return_value = self.__user_post(username="test_username",
                                        password="123abc")

        assert b'User created successfully' in return_value.data

    def test_try_insert_user_with_same_username_twice_not_allowed(self):
        """ Test insert user with the same username twice not allowed """
        return_value = self.__user_post(username="test_username",
                                        password="123abc")

        return_value = self.__user_post(username="test_username",
                                        password="12sdase4")

        assert b'A user with that username already exists' in return_value.data

    def __user_post(self, **kwargs):
        # kwargs should be a key value pair for username and password
        # Eg. user_post(username='test', password='123')
        return self.test_app.post('/api/users',
                                  data=dict(kwargs),
                                  follow_redirects=True)


if __name__ == '__main__':
    unittest.main()
