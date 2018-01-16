from flask_restful_swagger_2 import Resource, swagger
from app.models.comment import Comment
from app.resources.docs.comment import CommentResourceDoc


class CommentResource(Resource):
    @swagger.doc(CommentResourceDoc.get_by_id_docs())
    def get(self, id):
        return Comment.get_by_id(id), 200

    @classmethod
    def add_to_api_resource(cls, api):
        api.add_resource(CommentResource, '/api/comment/<string:id>')
