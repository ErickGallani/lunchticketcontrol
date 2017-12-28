class TicketResourceDoc:
    @staticmethod
    def get_docs():
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
