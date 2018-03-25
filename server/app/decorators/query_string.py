"""
Decorators for interprete the query strings and generate more
functional and easy to use query string objects
"""
from functools import wraps
from app.builders.filter_query_builder import FilterQueryBuilder

def request_filter(api_request):
    """
    Filter request decorator
    :param api_request: Api current request instance
    """
    def request_filter_decorator(resource_endpoint):
        """
        Create a filter object form the query string
        :param resource_endpoint: Current resource endpoint called
        """
        @wraps(resource_endpoint)
        def wrapper(*args, **kwargs):
            """ Wrapper preserving all the caller characteristics """
            filter_query = None

            if api_request and hasattr(api_request, 'args'):
                filter_query = FilterQueryBuilder(api_request.args).build()

            result = resource_endpoint(*args, filter_query, **kwargs)
            return result
        return wrapper
    return request_filter_decorator
