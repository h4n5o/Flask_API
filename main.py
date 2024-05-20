from flask import Flask, request
from flask_restful import Api, Resource

app = Flask (__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return{"data": "Hello World"}

    def post(self):
        return{"data": "Posted"}

    def put(self):
        data = request.get_json()
        return {"data": data}, 201

    def delete(self):
        return {"data": "Deleted"}, 204

api.add_resource(HelloWorld, "/helloworld")

if __name__ == "__main__":
    app.run(debug=True)
