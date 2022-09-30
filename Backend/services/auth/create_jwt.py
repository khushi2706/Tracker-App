from flask_jwt_extended import create_access_token

def createJwtToken(userId):
    jwt_token = create_access_token(identity=userId)
    return jwt_token