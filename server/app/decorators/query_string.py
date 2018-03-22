"""
Decorators for interprete the query strings and generate more
functional and easy to use query string objects
"""
from functools import wraps
from flask_restful_swagger_2 import request
from app.builders.filter_query_builder import FilterQueryBuilder

def request_filter(resource_endpoint):
    """ Create a filter object form the query string """
    @wraps(resource_endpoint)
    def wrapper(*args, **kwargs):
        """ Wrapper preserving all the caller characteristics """
        filter_query = None

        if request and hasattr(request, 'args'):
            filter_query = FilterQueryBuilder(request.args).build()

        result = resource_endpoint(*args, filter_query, **kwargs)
        return result
    return wrapper
