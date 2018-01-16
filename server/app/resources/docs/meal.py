class MealResourceDoc:
    @staticmethod
    def get_by_id_docs():
        return {
            'tags': ['meal'],
            'description': 'Returns json',
            'parameters': [
                {
                    'name': 'Meal Id',
                    'description': 'Meal Id',
                    'in': 'path',
                    'type': 'id'
                }
            ],
            'responses': {
                '200': {
                    'description': 'Meal for that day',
                    'examples': {
                        'application/json': {
                            'id': '22e4b4a8-f0b3-46ce-984f-75699ba337d0',
                            'created_at': '2018-01-16 13:45:54',
                            'picture': 'kjhgd672ui3hgasduaksdnasdj',
                            'title': 'This is an example title',
                            'description': 'A example description',
                            'date': '2018-01-16'
                        }
                    }
                }
            }
        }

    @staticmethod
    def delete_docs():
        return {}

    @staticmethod
    def put_docs():
        return {}


class MealListResourceDoc:
    @staticmethod
    def get_by_date_docs():
        return {
            'tags': ['meal'],
            'description': 'Returns json',
            'parameters': [
                {
                    'name': 'Meal Date',
                    'description': 'Meal Date',
                    'in': 'path',
                    'type': 'date'
                }
            ],
            'responses': {
                '200': {
                    'description': 'Meal for that day',
                    'examples': {
                        'application/json': {
                            'id': '22e4b4a8-f0b3-46ce-984f-75699ba337d0',
                            'created_at': '2018-01-16 13:45:54',
                            'picture': 'kjhgd672ui3hgasduaksdnasdj',
                            'title': 'This is an example title',
                            'description': 'A example description',
                            'date': '2018-01-16'
                        }
                    }
                }
            }
        }

    @staticmethod
    def post_docs():
        return {}
