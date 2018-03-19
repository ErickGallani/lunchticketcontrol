from flask_restful_swagger_2 import Resource, swagger
from app.models.comment import Comment
from app.resources.docs.comment import CommentResourceDoc

COMMENTS_WITHOUT_ID_RESOURCE_ENDPOINT = '/api/comments'
COMMENTS_WITH_ID_RESOURCE_ENDPOINT = '/api/comments/<uuid:id>'

class CommentResource(Resource):
    @swagger.doc(CommentResourceDoc.get_by_id_docs())
    def get(self, id):
        """
        Get comment by id
        :param id: User id
        """
        return Comment.get_by_id(id), 200

    @classmethod
    def add_to_api_resource(cls, api):
        """
        Add comment resources with id to the current api instace
        :param api: Application API instance
        """
        api.add_resource(CommentResource, COMMENTS_WITH_ID_RESOURCE_ENDPOINT)
