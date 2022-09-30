from flask import Flask, g
from datetime import datetime
import time, decimal, json
from flask_restx import Api
from models.config import Config as SETTING
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = SETTING.SECRET_KEY
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False

jwt = JWTManager(app)

@app.before_request
def before_request():
    g.start_time = time.time()
    g.response = {}


def myconverter(o):
    if isinstance(o, datetime.datetime) or isinstance(o, datetime.date):
        return o.__str__()
    elif isinstance(o, decimal.Decimal):
        return float(o)


@app.after_request
def after_request(res):
    print(time.time() - g.start_time)
    try:
        if (res.get_data()).decode("utf-8") == "null\n":
            res.set_data(json.dumps(g.response, default=myconverter))
        return res
    except Exception as e:
        return res

authorizations = {
    "api_key": {
        "type": "apiKey",
        "in": "header",
        "name": "AUTHORIZATION"
    }
}

api = Api(
    app,
    version="1.0",
    title="Madhku",
    description="Madhku API Documentation",
    security=["api_key"],
    prefix="/v1",
    authorizations=authorizations,
)
