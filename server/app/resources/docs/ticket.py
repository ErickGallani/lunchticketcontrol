""" Swagger documentation for ticket resources """

class TicketResourceDoc:
    """ Ticket resources swagger documentation """

    @staticmethod
    def get_docs():
        """ Get endpoint documentation """
        return {
            'tags': ['ticket'],
            'description': 'Returns json',
            'parameters': [
                {
                    'name': 'Ticket Date',
                    'description': 'Ticket date',
                    'in': 'path',
                    'type': 'string'
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
