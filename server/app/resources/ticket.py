from flask_restful_swagger_2 import Resource, swagger
from flask_jwt import jwt_required
from app.models.ticket import Ticket
from app.resources.docs.ticket import TicketResourceDoc


class TicketResource(Resource):
    @swagger.doc(TicketResourceDoc.get_docs())
    @jwt_required()
    def get(self, ticket_date):
        return Ticket.find_by_date(ticket_date), 200

    @classmethod
    def add_to_api_resource(cls, api):
        api.add_resource(TicketResource, '/api/tickets/<uuid:date>')
