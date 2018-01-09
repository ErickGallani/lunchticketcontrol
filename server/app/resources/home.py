from flask_restful_swagger_2 import Resource


class HomeResource(Resource):

    def get(self):
        return {'message': 'Home endpoint'}, 200

    @classmethod
    def add_to_api_resource(cls, api):
        api.add_resource(HomeResource, '/')
