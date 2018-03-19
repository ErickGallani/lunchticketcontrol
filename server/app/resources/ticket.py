""" Ticket resources """
from flask_restful_swagger_2 import Resource, swagger, request
from flask_jwt import jwt_required
from app.models.ticket import Ticket
from app.resources.docs.ticket import TicketResourceDoc

TICKETS_WITHOUT_ID_RESOURCE_ENDPOINT = '/api/tickets'
TICKETS_WITH_ID_RESOURCE_ENDPOINT = '/api/tickets/<uuid:id>'


class TicketResource(Resource):
    """ User resources """
    @swagger.doc(TicketResourceDoc.get_docs())
    def get(self):
        """
        Get user by id
        :param filter: Query string with filter[date] = timestamp of a date without hours
        """

        print(request.args)

        query_filter = request.args.get('filter')

        tickets_date = query_filter['date']

        return Ticket.find1_by_date(tickets_date), 200

    @classmethod
    def add_to_api_resource(cls, api):
        """
        Add ticket resources with id to the current api instace
        :param api: Application API instance
        """
        api.add_resource(TicketResource, TICKETS_WITHOUT_ID_RESOURCE_ENDPOINT)
