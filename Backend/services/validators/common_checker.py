from datetime import datetime
from models.auth import User
from models.enum import ActivityType

def usernameCheckerSignup(session, response, username):

    if username != None:
        userObj = (
            session.query(
                User,
            )
            .filter(
                User.username == username,
            )
            .first()
        )
        
        if userObj:
            response.setStatus(400)
            response.setError("Username is already taken")
            return None
        else:
            return username.lower()
    else:
        response.setStatus(400)
        response.setError("Please provide username")
        return None


def usernameCheckerLogin(session, response, username):
    if username != None:
        userObj = (
            session.query(
                User,
            )
            .filter(
                User.username == username.lower(),
            )
            .first()
        )
        if userObj:
            return userObj
        else:
            response.setStatus(400)
            response.setError("No User is exist with this username")
            return None
    else:
        response.setStatus(400)
        response.setError("Please provide username")
        return None


def passwordChecker(response, password):
    if password != None:
        if len(password) >= 8:
            return password
        else:
            response.setStatus(400)
            response.setError("Password length should be atleast 8 character")
            return None
    else:
        response.setStatus(400)
        response.setError("Please provide password")
        return None


def displayNameChecker(response, displayName):
    if displayName != None:
        if displayName != "":
            return True, displayName
        else:
            response.setStatus(400)
            response.setError("Invalid display name")
            return False, None
    else:
        response.setStatus(400)
        response.setError("Display name not provided")
        return False, None


def activityTitleChecker(response, activityTitle):
    try:
        if activityTitle != None:
            return activityTitle
        else:
            response.setStatus(400)
            response.setMessage("Bad request, activity title not provided")
            return None
    except:
        response.setStatus(400)
        response.setMessage("Bad request, invalid activity title")
        return None



def activityDistanceChecker(response, activityDistance):
    try:
        if activityDistance != None:
            return float(activityDistance)
        else :
            response.setStatus(400)
            response.setMessage("Bad request, activity distace not provided")
            return None
    except:
        response.setStatus(400)
        response.setMessage("Bad request, invalid activity distance")
        return None



def datetimeChecker(response, date):
    try:
        # Fri,30 Sep 2022 07:20:06 GMT    <--- date format
        return datetime.strptime(date, "%a,%d %b %Y %H:%M:%S %Z")
    except:
        response.setStatus(400)
        response.setMessage("Bad request, invalid date provided")
        return None


def activityTypeChecker(response, activityType):
    try:
        if activityType in list(ActivityType):
            return activityType
        else:
            response.setStatus(400)
            response.setMessage("Bad request, invalid activity type provided")
            return None
    except:
        response.setStatus(400)
        response.setMessage("Bad request, invalid date provided")
        return None