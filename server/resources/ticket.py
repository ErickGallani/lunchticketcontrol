from flask_restful import reqparse
from flask_restful_swagger_2 import Resource, swagger
from flask_jwt import jwt_required

class TicketResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id', 
        type=str,
        required=True,
        help='This field is required!'
    )

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
        # data = TicketResource.parser.parse_agrs()
        return {'ticket': 'new ticket'}, 200

    @classmethod
    def register(cls, api):
        api.add_resource(TicketResource, '/ticket')
