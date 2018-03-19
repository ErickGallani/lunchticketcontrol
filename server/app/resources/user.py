""" User resources """
from flask_restful import reqparse
from flask_restful_swagger_2 import Resource, swagger
from flask_jwt import jwt_required
from app.models.user import User
from app.models.ticket_history import TicketHistory
from app.resources.docs.user import UserResourceDoc
from app.resources.docs.ticket import TicketHistoryResourceDoc

USER_WITHOUT_ID_RESOURCE_ENDPOINT = '/api/users'
USER_WITH_ID_RESOURCE_ENDPOINT = '/api/users/<uuid:id>'
USER_WITH_ID_TICKETS_WITHOUT_ID_RESOURCE_ENDPOINT = '/api/users/<uuid:id>/tickets'
USER_WITH_ID_TICKETS_WITH_ID_RESOURCE_ENDPOINT = '/api/users/<uuid:id>/tickets/<uuid:id>'


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

    @jwt_required()
    def get(self):
        return User.get().get_all()

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
        """
        Add user resources to the current api instace
        :param api: Application API instance
        """
        api.add_resource(UserResource, USER_WITHOUT_ID_RESOURCE_ENDPOINT)


class UserWithIdResource(Resource):
    """ User with id resources """

    @swagger.doc(UserResourceDoc.get_by_id_docs())
    def get(self, id):
        """
        Get user by id
        :param id: User id
        """
        raise 'Testing exception'

    @classmethod
    def add_to_api_resource(cls, api):
        """
        Add user with id resources to the current api instace
        :param api: Application API instance
        """
        api.add_resource(UserWithIdResource, USER_WITH_ID_RESOURCE_ENDPOINT)


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
        """
        Add user tickets history resources to the current api instace
        :param api: Application API instance
        """
        api.add_resource(TicketHistoryResource, 
                         USER_WITH_ID_TICKETS_WITHOUT_ID_RESOURCE_ENDPOINT)
