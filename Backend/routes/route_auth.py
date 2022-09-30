from services.auth.login import login
from services.auth.signup import signup
from swagger_config import api
from flask_restx import reqparse, Resource
from flask import jsonify, request
from services.validators.validation_functions import validateParameters 
from routes.response import loginResponse, signupResponse

auth = api.namespace("auth", description="Auth Apis")

loginModel = reqparse.RequestParser()
loginModel.add_argument("username", type=str, required=True, help="Username of user", location="json")
loginModel.add_argument("password", type=str, required=True, help="Password of user", location="json")

signupModel = reqparse.RequestParser()
signupModel.add_argument("fname", type=str, required=True, help="Firstname of user", location="json")
signupModel.add_argument("username", type=str, required=True, help="Username of user", location="json")
signupModel.add_argument("password", type=str, required=True, help="Password of user", location="json")


@auth.route("/login")
class AuthLogin(Resource):
    @api.doc(responses=loginResponse)
    @api.expect(loginModel)
    def post(self):
        reqObj = validateParameters(request.json, ["username", "password"])
        output = login(reqObj)
        return jsonify(output)


@auth.route("/signup")
class AuthSignup(Resource):
    @api.doc(responses=signupResponse)
    @api.expect(signupModel)
    def post(self):
        reqObj = validateParameters(request.json, ["fname", "username", "password"])
        output = signup(reqObj)
        return jsonify(output)
