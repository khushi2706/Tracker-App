from models.conn import Session
from services.json_response import JsonResponse
from services.auth.create_jwt import createJwtToken
from services.validators.common_checker import passwordChecker, usernameCheckerLogin
from passlib.hash import sha256_crypt


def login(reqObj):
    response = JsonResponse()
    session = Session()

    try:
        data = {}
        userObj = usernameCheckerLogin(session, response, reqObj.get("username"))
        if userObj:
            password = passwordChecker(response, reqObj.get("password"))
            if password:
                if sha256_crypt.verify(password, userObj.password):
                    data = {
                        "user_id": userObj.user_id,
                        "username": userObj.username,
                        "fname": userObj.fname,
                        "created_at": userObj.created_at,
                        "jwt": createJwtToken(userId=userObj.user_id),
                    }
                    response.setStatus(200)
                    response.setMessage("Logged in successfully")
                else:
                    response.setStatus(403)
                    response.setError("Wrong password")

        response.setData(data)
        session.commit()

    except Exception as e:
        response.setStatus(500) # Internal error
        response.setError("Internal Server Error in Login => " + str(e))

    finally:
        session.close()
        return response.returnResponse()