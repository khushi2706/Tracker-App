from models.auth import User
from models.conn import Session
from services.json_response import JsonResponse
from services.validators.common_checker import  usernameCheckerSignup, passwordChecker
from models.config import Config as SETTING
from passlib.hash import sha256_crypt

def signup(reqObj):
    response = JsonResponse()
    session = Session()

    try:
        data = {}   
        username = usernameCheckerSignup(session, response, reqObj.get("username"))
        if username:
            password = passwordChecker(response, reqObj.get("password"))
            if password:
                userObj = User(
                        username = username,
                        password = sha256_crypt.hash(password),
                        fname = reqObj.get("fname"),
                    )
                session.add(userObj)
                session.flush()
                data = {
                    # "user_id": insertedUser.lastrowid,
                    "username": userObj.username,
                    "fname": userObj.fname,
                }

                response.setStatus(201)
                response.setMessage("Signup successfully")

        response.setData(data)
        session.commit()
    except Exception as e:
        response.setStatus(500) # Internal error
        response.setError("Internal Server Error in Signup => " + str(e))

    finally:
        session.close()
        return response.returnResponse()