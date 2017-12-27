import os
import unittest
import tempfile
from setup import app, api


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

    def test_send_post_without_username(self):
        rv = self.user_post(password="123abc")
        print(rv)
        print(rv.data)
        assert b'This field cannot be blank.' in rv.data

    def user_post(self, **kwargs):
        # kwargs should be a key value pair for username and password
        # Eg. user_post(username='test', password='123')
        return self.app.post('/user',
                             data=dict(kwargs),
                             follow_redirects=True)


if __name__ == '__main__':
    unittest.main()
