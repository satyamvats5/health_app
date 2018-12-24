from flask import Flask, request
from flask_restful import Api

from Util import config as Config

from Controller.Status import Status
from Controller.Calculate import Calculate


app = Flask(__name__)

api = Api(app)

api.add_resource(
    Status,
    Config.API_PATH + "/status",
    endpoint = "status_ep")

api.add_resource(
    Calculate,
    Config.API_PATH + "/calculate"
)

if __name__ == "__main__":

    try:
        app.run(debug = True, host = Config.API_CONF["host"], port = Config.API_CONF["port"])
    except Exception as e:
        print("Failed to start application:", e)