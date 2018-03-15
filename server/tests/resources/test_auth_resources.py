""" Tests for User resources """
import unittest
import json
from app import get_app, create_app, db


class AuthResourceTestCase(unittest.TestCase):
    """ Auth resources test case """
    def setUp(self):
        self.app = get_app(create_app)(config_name="testing")
        self.test_app = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.close()
            db.drop_all()

    def test_auth_valid_login(self):
        """ Test user login """
        return_value = self.__login('testuser', '123abc')
        data_json = json.loads(return_value.data.decode("utf-8"))
        
        assert 'access_token' in data_json, \
                "return does not have 'access_token' property - %r" % data_json

    def test_auth_logout(self):
        """ Test user logout """
        return_value = self.__logout()
        assert b'You were logged out' in return_value.data

    def test_auth_invalid_username_login(self):
        """ Test user login with invalid username """
        return_value = self.__login('invalid_testuser', '123abc')
        data_json = json.loads(return_value.data.decode("utf-8"))

        assert 'description' in data_json, \
                "return does not have 'description' property - %r" % data_json
        assert b'Invalid credentials' in data_json['description'], \
                "Description does not contain 'Invalid credentials'"

    def test_auth_invalid_password_login(self):
        """ Test user login with invalid password """
        return_value = self.__login('testuser', '123abc123')
        data_json = json.loads(return_value.data.decode("utf-8"))

        assert 'description' in data_json, \
                "return does not have 'description' property - %r" % data_json
        assert b'Invalid credentials' in data_json['description'], \
                "Description does not contain 'Invalid credentials'"

    def __login(self, username, password):
        return self.app.post('/auth',
                             data=dict(
                                 username=username,
                                 password=password
                             ), follow_redirects=True)

    def __logout(self):
        return self.app.get('/logout', follow_redirects=True)


if __name__ == '__main__':
    unittest.main()
