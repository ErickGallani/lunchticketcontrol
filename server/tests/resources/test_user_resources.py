import unittest
from app import create_app, db


class UserResourceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.close()
            db.drop_all()

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
