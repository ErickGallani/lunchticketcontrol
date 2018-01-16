from flask_jwt import jwt_required
from flask_restful import reqparse
from flask_restful_swagger_2 import Resource, swagger
from app.models.meal import Meal
from app.resources.docs.meal import MealResourceDoc, MealListResourceDoc


class MealResource(Resource):
    @swagger.doc(MealResourceDoc.get_by_id_docs())
    def get(self, id):
        return Meal.get(id), 200

    @swagger.doc(MealResourceDoc.delete_docs())
    @jwt_required()
    def delete(self, id):
        return '', 204

    @swagger.doc(MealResourceDoc.put_docs())
    @jwt_required()
    def put(self, id):
        parser = reqparse.RequestParser()
        args = parser.parse_args()
        return '', 201

    @classmethod
    def add_to_api_resource(cls, api):
        api.add_resource(MealResource, '/api/meals/<uuid:id>')


class MealListResource(Resource):
    @swagger.doc(MealListResourceDoc.get_by_date_docs())
    def get(self):
        parser = reqparse.RequestParser()
        args = parser.parse_args()
        date = args['date']
        return Meal.get_by_date(date), 200

    @swagger.doc(MealListResourceDoc.post_docs())
    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        args = parser.parse_args()
        return '', 201

    @classmethod
    def add_to_api_resource(cls, api):
        api.add_resource(MealListResource, '/api/meals')
