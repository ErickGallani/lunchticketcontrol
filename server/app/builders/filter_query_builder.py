"""
Filter query builder from a request
Example:
https://localhost:5050/api/tickets?filter[date]=1521417600&filter[uder_id]=15
will build a query filter object with prop filters like
filters = {
    'date': 1521417600,
    'uder_id': '67df3964-e153-413b-a0d8-cbdc321c77b3'
}
"""
import re

class FilterQueryBuilder(object):
    """ Builder from the filter query string """

    def __init__(self, query_string_args):
        if query_string_args:
            self.filters = {}
            self.query_string = query_string_args
            self.get_attr_regex_pattern = r"\[(?P<filter_value>.*?)\]"
            self.regex = re.compile(self.get_attr_regex_pattern)

    def build(self):
        """
        Build the filter query object compiling the query string in to the object
        """
        for arg in self.query_string:
            attr = self.regex.search(arg).group("filter_value")
            self.filters[attr] = self.query_string[arg]

        return self
