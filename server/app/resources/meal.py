from flask_restful_swagger_2 import Resource, swagger
from app.models.meal import Meal
from app.resources.docs.meal import MealResourceDoc


class MealResource(Resource):
    @swagger.doc(MealResourceDoc.get_by_date_docs())
    def get(self, date):
        return Meal.get_by_date(date), 200

    @classmethod
    def add_to_api_resource(cls, api):
        api.add_resource(MealResource, '/api/meal/<string:id>')
