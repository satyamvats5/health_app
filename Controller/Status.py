from flask_restful import Resource

class Status(Resource):
    def post(self):
        return 200