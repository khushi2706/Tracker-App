from models.conn import Session
from services.json_response import JsonResponse
from services.validators.common_checker import activityDistanceChecker, activityTitleChecker, activityTypeChecker, datetimeChecker
from flask_jwt_extended.utils import get_jwt_identity
from dataclasses import asdict
from models.activity import Activity


def createActivity(reqObj):
    response = JsonResponse()
    session = Session()
    userId = get_jwt_identity()

    try:
        data = {}
        activityDistance = None
        activityType = None
        startAtDatetime = None
        endAtDatetime = None

        activityTitle = activityTitleChecker(response, reqObj.get("title"))

        if activityTitle != None:
            activityDistance = activityDistanceChecker(response, reqObj.get("distance"))
        
        if activityDistance != None:
            activityType = activityTypeChecker(response, reqObj.get("activity_type"))

        if activityType != None:
            startAtDatetime = datetimeChecker(response, reqObj.get("start_at"))
            
        if startAtDatetime != None:
            endAtDatetime = datetimeChecker(response, reqObj.get("end_at"))

        if endAtDatetime != None:
            activityObj = Activity(
                title = activityTitle,
                distance = activityDistance,
                activity_type = activityType,
                note = reqObj.get("note"),
                start_at = startAtDatetime,
                end_at = endAtDatetime,
                user_id = userId,
            )
            print(activityObj)
            session.add(activityObj)
            session.flush()
            data = asdict(activityObj)
            response.setStatus(201)
            response.setMessage("Activity added successfully !!")

        response.setData(data)
        session.commit()

    except Exception as e:
        response.setStatus(500) # Internal error
        response.setError("Internal Server Error in Create Activity => " + str(e))

    finally:
        session.close()
        return response.returnResponse()