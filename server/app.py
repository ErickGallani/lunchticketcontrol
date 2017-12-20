from flask_restful_swagger_2 import Resource, swagger
from setup import api, app

class HelloWorld(Resource):
    @swagger.doc({
        'tags': ['helloworld'],
        'description': 'Returns json',
        'responses': {
            '200': {
                'description': 'Hello World',
                'examples': {
                    'application/json': {
                        'id': 1,
                        'name': 'somebody'
                    }
                }
            }
        }
    })
    def get(self):
        return {'hello': 'world'}, 200

api.add_resource(HelloWorld, '/api')

if __name__ == '__main__':
    app.run(debug=True)