from math import ceil
from models.conn import Session
from services.json_response import JsonResponse
from services.validators.common_checker import datetimeChecker
from flask_jwt_extended.utils import get_jwt_identity
from dataclasses import asdict
from models.activity import Activity
from sqlalchemy.sql.expression import and_
from datetime import datetime, timedelta
from sqlalchemy.sql.functions import func
from sqlalchemy import extract


def getActivities(reqObj):
    response = JsonResponse()
    session = Session()
    userId = get_jwt_identity()

    try:
        data = {}
        if reqObj.get("period") == None:
            # give all activity object
            activityObjs = (
                session.query(
                        Activity
                )
                .filter(
                    Activity.user_id == userId
                )
            )
            data = {
                "activities": [
                    asdict(activity)
                    for activity in activityObjs
                ],

            }

            response.setStatus(200)
            response.setMessage("Activities fetched successfully !!")

        else:
            if reqObj.get("period") == "weekly":
                # give stats for weekly
                if reqObj.get("date"):
                    periodDatetime = datetimeChecker(response, reqObj.get("date"))
                    if periodDatetime:
                        activityObjs = (
                            session.query(
                                    Activity,
                                    func.sum(Activity.distance).label("total_distance"),
                                    func.count(Activity.activity_id).label("total_ride"),
                                    func.sum(extract("minute", Activity.end_at) - extract("minute", Activity.start_at)).label("total_minute"),
                                    func.sum(extract("hour", Activity.end_at) - extract("hour", Activity.start_at)).label("total_hour"),
                                    extract("day", Activity.start_at),
                                    extract("month", Activity.start_at),
                                    extract("year", Activity.start_at),
                            )
                            .filter(
                                and_(
                                    Activity.user_id == userId,
                                    Activity.start_at >=( periodDatetime.date() - timedelta(days=7))
                                )
                            )
                            .group_by(
                                extract("day", Activity.start_at),
                                extract("month", Activity.start_at),
                                extract("year", Activity.start_at)
                            )
                            .all()
                        )
                        data = {
                            "activities": [
                                {
                                    "activity": asdict(activity[0]),
                                    "total_distance" : activity[1],
                                    "total_ride" : activity[2],
                                    **generateProperHourMinute(hour= activity[4], minute=activity[3]),
                                    "date": generateDatetimeObj(
                                        day=activity[5],
                                        month=activity[6],
                                        year=activity[7]
                                    ),
                                }
                                for activity in activityObjs
                            ],
                        }
                        response.setStatus(200)
                        response.setMessage("Activities fetched successfully !!")
                else:
                    response.setStatus(400)
                    response.setMessage("Date not provided")
            else:
                # give stats for all activities
                activityObjs = (
                    session.query(
                            Activity,
                            func.sum(Activity.distance).label("total_distance"),
                            func.count(Activity.activity_id).label("total_ride"),
                            func.sum(extract("minute", Activity.end_at) - extract("minute", Activity.start_at)).label("total_minute"),
                            func.sum(extract("hour", Activity.end_at) - extract("hour", Activity.start_at)).label("total_hour"),
                            extract("day", Activity.start_at),
                            extract("month", Activity.start_at),
                            extract("year", Activity.start_at),
                    )
                    .filter(
                        Activity.user_id == userId
                    )
                    .group_by(
                        extract("day", Activity.start_at),
                        extract("month", Activity.start_at),
                        extract("year", Activity.start_at)
                    )
                    .all()
                )
                # print(activityObjs)
                data = {
                    "activities": [
                        {
                            "activity": asdict(activity[0]),
                            "total_distance" : activity[1],
                            "total_ride" : activity[2],
                            **generateProperHourMinute(hour= activity[4], minute=activity[3]),
                            "date": generateDatetimeObj(
                                day=activity[5],
                                month=activity[6],
                                year=activity[7]
                            ),
                        }
                        for activity in activityObjs
                    ],

                }

                response.setStatus(200)
                response.setMessage("Activities stats fetched successfully !!")

        response.setData(data)

    except Exception as e:
        response.setStatus(500) # Internal error
        response.setError("Internal Server Error in Get Activities => " + str(e))

    finally:
        session.close()
        return response.returnResponse()


def generateDatetimeObj(day, month, year):
    return datetime.strptime(f"{day} {month} {year}", "%d %m %Y")


def generateProperHourMinute(hour, minute):
    if minute >=0 :
        return {
            "total_hour": hour,
            "total_minute": minute,
            "formatted_time": hour + minute/60
        }
    else:
        return {
            "total_hour": hour + ceil(minute/60),
            "total_minute": minute%60,
            "formatted_time": hour + minute/60
        }
