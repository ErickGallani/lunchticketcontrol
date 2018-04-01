""" Ticket resources """
from datetime import datetime
from flask_restful_swagger_2 import Resource, swagger, request
from app.models.ticket import Ticket, TicketSchema
from app.resources.docs.ticket import TicketResourceDoc
from app.decorators.query_string import request_filter
from app.helpers.jsonify_response import jsonify_response
from app.helpers.try_parse import TryParse

TICKETS_WITHOUT_ID_RESOURCE_ENDPOINT = '/api/tickets'
TICKETS_WITH_ID_RESOURCE_ENDPOINT = '/api/tickets/<uuid:id>'

class TicketResource(Resource):
    """ User resources """
    def __init__(self):
        self.tickets_schema = TicketSchema(many=True)

    @swagger.doc(TicketResourceDoc.get_docs())
    @request_filter(request)
    def get(self, request_args):
        """
        Get user by id
        :param filter: Query string with filter[date] = timestamp of a date without hours
        """
        if 'date' in request_args.filters:
            ticket_timestamp = TryParse.to_int(None, request_args.filters['date'])
            date_filter = TryParse.from_timestamp_to_datetime(None, ticket_timestamp)
        else:
            date_filter = datetime(2018, 3, 25)

        tickets = Ticket.find_by_date(date_filter)

        result = self.tickets_schema.dump(tickets)
        return jsonify_response(result.data, 200)

    @classmethod
    def add_to_api_resource(cls, api):
        """
        Add ticket resources with id to the current api instace
        :param api: Application API instance
        """
        api.add_resource(TicketResource, TICKETS_WITHOUT_ID_RESOURCE_ENDPOINT)
