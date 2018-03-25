""" Tests for filter query decorator """
import unittest
from werkzeug.datastructures import ImmutableMultiDict
from app.decorators.query_string import request_filter

WRAPPER_METHOD = lambda x: x

class RequestSimulacrum(object):

    def __init__(self, args):
        self.args = args

class FilterQueryDecoratorTestCase(unittest.TestCase):

    def test_request_with_empty_query_string(self):
        # arrange
        filters_length = 0
        request_simulacrum = RequestSimulacrum([])

        # act
        response = request_filter(request_simulacrum)(WRAPPER_METHOD)()

        # assert
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.filters)
        self.assertEqual(filters_length, len(response.filters))

    def test_request_with_null_query_string(self):
        # arrange
        filters_length = 0
        request_simulacrum = RequestSimulacrum(None)

        # act
        response = request_filter(request_simulacrum)(WRAPPER_METHOD)()

        # assert
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.filters)
        self.assertEqual(filters_length, len(response.filters))

    def test_request_with_one_correct_query_string(self):
        # arrange
        filters_length = 1
        date_value = 123456789
        args = ImmutableMultiDict(
            [
                ("filter[date]", date_value)
            ])

        request_simulacrum = RequestSimulacrum(args)

        # act
        response = request_filter(request_simulacrum)(WRAPPER_METHOD)()

        # assert
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.filters)
        self.assertEqual(filters_length, len(response.filters))
        self.assertEqual(date_value, response.filters['date'])

    def test_request_with_one_correct_query_string(self):
        # arrange
        filters_length = 2
        date_value = 123456789
        user_id = 15
        args = ImmutableMultiDict(
            [
                ("filter[date]", date_value),
                ("filter[user_id]", user_id)
            ])

        request_simulacrum = RequestSimulacrum(args)

        # act
        response = request_filter(request_simulacrum)(WRAPPER_METHOD)()

        # assert
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.filters)
        self.assertEqual(filters_length, len(response.filters))
        self.assertEqual(date_value, response.filters['date'])
        self.assertEqual(user_id, response.filters['user_id'])
