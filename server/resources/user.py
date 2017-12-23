from flask_restful_swagger_2 import Resource

class UserResource(Resource):
    def get(self):
        return {'user': 'user'}, 200

    def post(self):
        return {'user': 'user'}, 201

    @classmethod
    def register(cls, api):
        api.add_resource(UserResource, '/user')
