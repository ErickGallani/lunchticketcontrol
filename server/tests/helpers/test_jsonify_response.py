import unittest
import json
from app import get_app, create_app
from app.helpers.jsonify_response import jsonify_response

class JsonifyResponseTestCase(unittest.TestCase):

    def setUp(self):
        self.app = get_app(create_app)(config_name="testing")
        self.test_app = self.app.test_client()

    def test_jsonify_response_correct_response_with_success_and_status_200(self):
        # arrange
        valid_json_obj = {
            'name': 'Test',
            'age': 20,
            'msg': 'Random msg'
        }

        http_response = None
        status_code = 200
        content_type = 'application/json'

        # act
        with self.app.test_request_context():
            http_response = jsonify_response(valid_json_obj, status_code)

        data_json = json.loads(http_response.data.decode("utf-8"))

        # assert
        self.assertIsNotNone(http_response)
        self.assertEqual(status_code, http_response.status_code)
        self.assertEqual(content_type, http_response.content_type)
        self.assertEqual(valid_json_obj['name'], data_json['data']['name'])
        self.assertEqual(valid_json_obj['age'], data_json['data']['age'])
        self.assertEqual(valid_json_obj['msg'], data_json['data']['msg'])
