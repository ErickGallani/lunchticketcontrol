from flask_restful_swagger_2 import Resource, swagger
from flask_jwt import jwt_required
from app.models.ticket import Ticket


class TicketResource(Resource):
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
    def get(self, ticket_date):
        return Ticket.find_by_date(ticket_date)

    @classmethod
    def add_to_api_resource(cls, api):
        api.add_resource(TicketResource, '/ticket/<string:ticket_date>')
