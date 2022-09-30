from models.conn import Session
from services.json_response import JsonResponse
from flask_jwt_extended.utils import get_jwt_identity
from models.activity import Activity
from sqlalchemy.sql.expression import and_

def deleteActivity(activityId):
    response = JsonResponse()
    session = Session()
    userId = get_jwt_identity()

    try:
        data = {}

        if activityId:
            activityObj = (
                session.query(
                    Activity
                )
                .filter(
                    and_(
                        Activity.activity_id == activityId,
                        Activity.user_id == userId
                    )
                )
                .first()
            )
            print(activityObj)
            if activityObj:
                session.delete(activityObj)
                session.flush()
                response.setStatus(200)
                response.setMessage("Activity deleted successfully !!")
            else:
                response.setStatus(400)
                response.setMessage("No Activity exists with this id")

        response.setData(data)
        session.commit()

    except Exception as e:
        response.setStatus(500) # Internal error
        response.setError("Internal Server Error in Delete Activity => " + str(e))

    finally:
        session.close()
        return response.returnResponse()