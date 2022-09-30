from services.activity.create_activity import createActivity
from services.activity.delete_activity import deleteActivity
from services.activity.edit_activity import editActivity
from services.activity.get_activities import getActivities
from services.activity.get_activity import getActivity
from swagger_config import api
from flask_restx import reqparse, Resource
from flask import jsonify, request
from services.validators.validation_functions import validateParameters 
from flask_jwt_extended import jwt_required


activity = api.namespace("activity", description="Activity Apis")

createActivityModel = reqparse.RequestParser()
createActivityModel.add_argument("title", type=str, required=True, help="Activity title", location="json")
createActivityModel.add_argument("distance", type=int, required=True, help="Travel distance during activity", location="json")
createActivityModel.add_argument("activity_type", type=int, required=True, help="Type of activity", location="json")
createActivityModel.add_argument("note", type=str, required=False, help="Note for activity", location="json")
createActivityModel.add_argument("start_at", type=str, required=True, help="Starting time of activity", location="json")
createActivityModel.add_argument("end_at", type=str, required=True, help="Ending time of activity", location="json")

getActivityModel = reqparse.RequestParser()
getActivityModel.add_argument("period", type=str, required=False, help="Type period (weekly, all)", location="args")
getActivityModel.add_argument("date", type=str, required=False, help="Date for weekly stats", location="args")

deleteActivityModel = reqparse.RequestParser()
deleteActivityModel.add_argument("activity_id", type=str, required=True, help="Activity id", location="json")


@activity.route("/")
class Activity(Resource):
    @jwt_required()
    @api.doc(responses={200: "OK"})
    @api.expect(createActivityModel)
    def post(self):
        reqObj = validateParameters(request.json, ["title", "distance", "activity_type", "note", "start_at", "end_at"])
        output = createActivity(reqObj)
        return jsonify(output)


    @jwt_required()
    @api.doc(responses={200: "OK"})
    @api.expect(getActivityModel)
    def get(self):
        reqObj = validateParameters(request.args, ["period", "date"])
        output = getActivities(reqObj)
        return jsonify(output)


@activity.route("/<int:activityId>")
class SingleActivity(Resource):
    @jwt_required()
    @api.doc(responses={200: "OK"})
    def get(self, activityId):
        output = getActivity(activityId)
        return jsonify(output)
    

    @jwt_required()
    @api.doc(responses={200: "OK"})
    @api.expect(createActivityModel)
    def put(self, activityId):
        reqObj = validateParameters(request.json, ["title", "distance", "activity_type", "note", "start_at", "end_at"])
        output = editActivity(reqObj, activityId)
        return jsonify(output)
    

    @jwt_required()
    @api.doc(responses={200: "OK"})
    @api.expect(deleteActivityModel)
    def delete(self, activityId):
        output = deleteActivity(activityId)
        return jsonify(output)

