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

    FILTER_GROUP_NAME = 'filter_value'

    def __init__(self, query_string_args):
        # Match any string starting with filter '^filter'
        # followed by a pair of brackets '[]' having something
        # inside the brackets must have a text with at least
        # one word '\w+' and create a group named 'filter_value'
        # (?P<filter_value>\w+?)
        self.get_attr_regex_pattern = \
            r"^filter\[(?P<%s>\w+?)\]" % self.FILTER_GROUP_NAME

        self.filters = {}
        self.query_string = query_string_args
        self.regex = re.compile(self.get_attr_regex_pattern)

    def build(self):
        """
        Build the filter query object compiling the query string in to the object
        """
        if self.query_string:
            for arg in self.query_string:
                attr = self.regex.search(arg)
                if attr:
                    filter_attr = attr.group(self.FILTER_GROUP_NAME)
                    self.filters[filter_attr] = self.query_string[arg]

        return self
