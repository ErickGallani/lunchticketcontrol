import unittest
from datetime import datetime
from app.helpers.try_parse import TryParse

class TicketTryParseTestCase(unittest.TestCase):

    def test_try_parse_int_valid_value_return_correct_value(self):
        # arrange
        valid_int_value = "123456789"
        expected_value = 123456789

        # act
        result = TryParse.to_int(None, valid_int_value)

        # assert
        self.assertEqual(expected_value, result)

    def test_try_parse_int_invalid_value_return_default_value(self):
        # arrange
        invalid_int_value = "abcdef"
        expected_value = None

        # act
        result = TryParse.to_int(None, invalid_int_value)

        # assert
        self.assertEqual(expected_value, result)

    def test_try_parse_float_valid_value_return_correct_value(self):
        # arrange
        valid_float_value = "140.45"
        expected_value = 140.45

        # act
        result = TryParse.to_float(None, valid_float_value)

        # assert
        self.assertEqual(expected_value, result)

    def test_try_parse_float_invalid_value_return_default_value(self):
        # arrange
        valid_float_value = "140.abc"
        expected_value = 0

        # act
        result = TryParse.to_float(0, valid_float_value)

        # assert
        self.assertEqual(expected_value, result)

    def test_try_parse_timestamp_valid_value_return_correct_datetime_value(self):
        # arrange
        valid_float_value = 1522537200
        expected_value = datetime(2018, 4, 1)

        # act
        result = TryParse.from_timestamp_to_datetime(None, valid_float_value)

        # assert
        self.assertEqual(str(expected_value), str(result))

    def test_try_parse_timestamp_valid_str_value_return_correct_datetime_value(self):
        # arrange
        valid_float_value = "1522537200"
        expected_value = datetime(2018, 4, 1)

        # act
        result = TryParse.from_timestamp_to_datetime(None, valid_float_value)

        # assert
        self.assertEqual(str(expected_value), str(result))

    def test_try_parse_timestamp_invalid_int_value_return_default_value(self):
        # arrange
        valid_float_value = 12312
        expected_value = None

        # act
        result = TryParse.from_timestamp_to_datetime(None, valid_float_value)

        # assert
        self.assertEqual(expected_value, result)

    def test_try_parse_timestamp_invalid_str_value_return_default_value(self):
        # arrange
        valid_float_value = "abcde"
        expected_value = None

        # act
        result = TryParse.from_timestamp_to_datetime(None, valid_float_value)

        # assert
        self.assertEqual(expected_value, result)
