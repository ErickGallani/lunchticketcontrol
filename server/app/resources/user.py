""" User resources """
from flask_restful import reqparse
from flask_restful_swagger_2 import Resource, swagger
from flask_jwt import jwt_required
from app.models.user import User
from app.models.ticket_history import TicketHistory
from app.resources.docs.ticket import TicketHistoryResourceDoc

USER_RESOURCE_ENDPOINT = '/api/users/<uuid:id>'


class UserResource(Resource):
    """ User resources """
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank.")

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank.")

    def get(self, id):
        raise 'Testing exception'

    def post(self):
        """ Insert user data """
        data = UserResource.parser.parse_args()

        if User.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = User(data['username'], data['password'])
        user.save()

        return {"message": "User created successfully."}, 201

    @classmethod
    def add_to_api_resource(cls, api):
        """ Add user resources to the current api instace """
        api.add_resource(UserResource, USER_RESOURCE_ENDPOINT)


class TicketHistoryResource(Resource):
    """ User tickets history """
    @swagger.doc(TicketHistoryResourceDoc.get_docs())
    @jwt_required()
    def get(self, id):
        """
        Get all tickets from user history
        :param id: User id
        """
        return TicketHistory.get_by_user_id(id), 200

    @classmethod
    def add_to_api_resource(cls, api):
        """ Add user tickets history resources to the current api instace """
        api.add_resource(TicketHistoryResource, '/api/users/<uuid:id>/tickets')
