from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

class Helloworld(Resource):
	def get(self):
		return {"about": "hello world"}
		
	def post(self):
		some_json = request.get_json()
		return {"you sent": some_json}, 201
		
class Multi(Resource):
	def get(self, num):
		return {"result": num*num}
		
api.add_resource(Helloworld, '/')
api.add_resource(Multi, "/multi/<int:num>")

if __name__ == '__main__':
	app.run(port=8888)