from flask_restful_swagger_2 import Resource, swagger
from setup import api, app
from flask_jwt import jwt_required

class Ticket(Resource):
    @swagger.doc({
        'tags': ['ticket'],
        'description': 'Returns json',
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
    })
    @jwt_required()
    def get(self):
        return {'ticket': 'new ticket'}, 200

api.add_resource(HelloWorld, '/ticket')

if __name__ == '__main__':
    app.run()