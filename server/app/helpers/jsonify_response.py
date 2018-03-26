""" Helper to make a json response for complex objects """
from flask import jsonify, make_response

def jsonify_response(response_obj, status_code):
    """
    Create a response from a json
    :param response_obj: The object to return, can be a complex object
                         an array, dict, string, any kind
    :param status_code: The response status code. Eg.: 200, 400, 404
    """
    return make_response(jsonify({'data': response_obj}), status_code)
