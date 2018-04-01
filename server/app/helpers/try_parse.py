""" Module for all parse safe methods """
from datetime import datetime

class TryParse(object):
    """ Safe parse values preventing exceptions """
    @staticmethod
    def to_int(default_value, value):
        """
        Parse an value to int
        :param default_value: Default value to be returned if the parse fails
        :param value: Value to be parsed to int
        :return: return int value or default value cause the parse failed
        """
        sint = TryParse._try_parse(default_value, ValueError)(int)
        return sint(value)

    @staticmethod
    def to_float(default_value, value):
        """
        Parse an value to float
        :param default_value: Default value to be returned if the parse fails
        :param value: Value to be parsed to float
        :return: return float value or default value cause the parse failed
        """
        sfloat = TryParse._try_parse(default_value, ValueError)(float)
        return sfloat(value)

    @staticmethod
    def from_timestamp_to_datetime(default_value, timestamp):
        """
        Parse a timestamp to datetime
        :param default_value: Default value to be returned if the parse fails
        :param timestamp: Timestamp to be parsed to datetime
        :return: return datetime from timestamp value or
                        default value cause the parse failed
        """
        # if the timestamp is type of string, try to parse to int
        if isinstance(timestamp, str):
            timestamp = TryParse.to_float(0, timestamp)

        sdatetime = TryParse._try_parse(default_value, Exception)(datetime.fromtimestamp)
        return sdatetime(timestamp)

    @staticmethod
    def _try_parse(default_val, ignore_exception):
        """ Method to ignoring exception from a function
            and return the default value when raise exception
        :param default_value: Default value to be returned when exception occurs
        :param ignore_exception: Exception to be ignored
        """
        def dec(function):
            """ Func decorator """
            def _dec(*args, **kwargs):
                try:
                    return function(*args, **kwargs)
                except ignore_exception:
                    return default_val
            return _dec
        return dec
