from flask_restful import reqparse
from flask_restful_swagger_2 import Resource
from app.models.user import User


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
