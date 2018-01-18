from flask_restful import reqparse
from flask_restful_swagger_2 import Resource, swagger
from flask_jwt import jwt_required
from app.models.user import User
from app.models.ticket_history import TicketHistory
from app.resources.docs.ticket import TicketHistoryResourceDoc


class UserResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank.")

    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank.")

    def post(self):
        data = UserResource.parser.parse_args()

        if User.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = User(data['username'], data['password'])
        user.save()

        return {"message": "User created successfully."}, 201

    @classmethod
    def add_to_api_resource(cls, api):
        api.add_resource(UserResource, '/api/users')


class TicketHistoryResource(Resource):
    @swagger.doc(TicketHistoryResourceDoc.get_docs())
    @jwt_required()
    def get(self, id):
        return TicketHistory.get(id), 200

    @classmethod
    def add_to_api_resource(cls, api):
        api.add_resource(TicketHistoryResource, '/api/users/<uuid:id>/tickets')
