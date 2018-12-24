from flask import Flask, request
from flask_restful import Api

from Util import config as Config

from Controller.Status import Status


app = Flask(__name__)

api = Api(app)

api.add_resource(
    Status,
    Config.API_PATH + "/status",
    endpoint = "status_ep")

if __name__ == "__main__":

    try:
        app.run(debug = True, host = Config.API_CONF["host"], port = Config.API_CONF["port"])
    except Exception as e:
        print("Failed to start application:", e)