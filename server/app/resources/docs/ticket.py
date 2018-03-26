""" Swagger documentation for ticket resources """

class TicketResourceDoc:
    """ Ticket resources swagger documentation """

    @staticmethod
    def get_docs():
        """ Get endpoint documentation """
        return {
            'tags': ['ticket'],
            'description':
                'Get all tickets by date. ' \
                'If no date is passed as filter query or the ' \
                'query parameter is in the wrong format, the today date will be used',
            'parameters': [
                {
                    'name': 'filter[date]',
                    'description': 'Filter tickets by date',
                    'in': 'query',
                    'type': 'timestamp'
                }
            ],
            'responses': {
                '200': {
                    'description': 'Lunch tickets',
                    'examples': {
                        'application/json': {
                            'id': 1,
                            'name': 'ticket name'
                        }
                    }
                }
            }
        }


class TicketHistoryResourceDoc:
    """ Ticket history resources swagger documentation """

    @staticmethod
    def get_docs():
        """ Get endpoint documentation """
        return {}
