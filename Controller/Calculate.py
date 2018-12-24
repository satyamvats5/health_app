from flask_restful import Resource
from Model.Calc_bmi import calc_bmi as c_bmi
from flask import request

class Calculate(Resource):
    def post(self):
        req = request.get_json(force = True)
        print(req)
        req_id = req["id"]
        calc_func = req["func"]

        if calc_func == "bmi":
            return c_bmi(req)