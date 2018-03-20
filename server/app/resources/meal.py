""" Meal resources """

from flask_jwt import jwt_required
from flask_restful import reqparse
from flask_restful_swagger_2 import Resource, swagger
from app.models.meal import Meal
from app.resources.docs.meal import MealWithIdResourceDoc, MealResourceDoc

MEALS_WITHOUT_ID_RESOURCE_ENDPOINT = '/api/meals'
MEALS_WITH_ID_RESOURCE_ENDPOINT = '/api/meals/<uuid:id>'


class MealResource(Resource):
    @swagger.doc(MealResourceDoc.get_by_date_docs())
    def get(self):
        # parser = reqparse.RequestParser()
        # args = parser.parse_args()
        # date = args['date']
        # return Meal.get_by_date(date), 200
        return '', 200

    @swagger.doc(MealResourceDoc.post_docs())
    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        args = parser.parse_args()
        return '', 201

    @classmethod
    def add_to_api_resource(cls, api):
        """
        Add meal resources to the current api instace
        :param api: Application API instance
        """
        api.add_resource(MealResource, MEALS_WITHOUT_ID_RESOURCE_ENDPOINT)


class MealWithIdResource(Resource):
    """ Meal resources """
    @swagger.doc(MealWithIdResourceDoc.get_by_id_docs())
    def get(self, id):
        """ Get meal by id endpoint """
        return Meal.get(id), 200

    @swagger.doc(MealWithIdResourceDoc.delete_docs())
    @jwt_required()
    def delete(self, id):
        """ Delete meal by id endpoint """
        return '', 204

    @swagger.doc(MealWithIdResourceDoc.put_docs())
    @jwt_required()
    def put(self, id):
        """ Edit meal by id endpoint """
        parser = reqparse.RequestParser()
        args = parser.parse_args()
        return '', 201

    @classmethod
    def add_to_api_resource(cls, api):
        """
        Add meal resources with id to the current api instace
        :param api: Application API instance
        """
        api.add_resource(MealWithIdResource, MEALS_WITH_ID_RESOURCE_ENDPOINT)
