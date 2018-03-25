""" Ticket resources """
from flask_restful_swagger_2 import Resource, swagger, request
from app.models.ticket import Ticket
from app.resources.docs.ticket import TicketResourceDoc
from app.decorators.query_string import request_filter

TICKETS_WITHOUT_ID_RESOURCE_ENDPOINT = '/api/tickets'
TICKETS_WITH_ID_RESOURCE_ENDPOINT = '/api/tickets/<uuid:id>'


class TicketResource(Resource):
    """ User resources """
    @swagger.doc(TicketResourceDoc.get_docs())
    @request_filter(request)
    def get(self, request_args):
        """
        Get user by id
        :param filter: Query string with filter[date] = timestamp of a date without hours
        """
        print(request_args)

        return Ticket.find_by_date(request_args.filters['date']), 200

    @classmethod
    def add_to_api_resource(cls, api):
        """
        Add ticket resources with id to the current api instace
        :param api: Application API instance
        """
        api.add_resource(TicketResource, TICKETS_WITHOUT_ID_RESOURCE_ENDPOINT)
