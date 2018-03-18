""" Swagger documentation for comment resources """

class CommentResourceDoc:
    """ Comment resources swagger documentation """

    @staticmethod
    def get_by_id_docs():
        """ Get by id endpoint documentation """
        return {
            'tags': ['comment'],
            'description': 'Returns json',
            'parameters': [
                {
                    'name': 'Comment id',
                    'description': 'Comment id',
                    'in': 'path',
                    'type': 'UUID'
                }
            ],
            'responses': {
                '200': {
                    'description': 'Comment',
                    'examples': {
                        'application/json': {
                            'id': '22e4b4a8-f0b3-46ce-984f-75699ba337d0',
                            'created_at': '2018-01-16 13:45:54',
                            'text': 'My comment'
                        }
                    }
                }
            }
        }
