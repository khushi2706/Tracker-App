from dotenv import load_dotenv
from models.conn import Base, createDatabase, engine
from flask_cors import CORS, cross_origin

load_dotenv()


from swagger_config import app
import os
import routes.route_auth
import routes.route_activity
from models.config import Config as SETTING


def initilize_db():
    from models.auth import User 
    from models.activity import Activity 

    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    Cors = CORS(app)
    CORS(app, resources={r'/*': {'origins': '*'}},CORS_SUPPORTS_CREDENTIALS = True)
    app.config['CORS_HEADERS'] = 'Content-Type'
    createDatabase()
    initilize_db()
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    app.run(port=SETTING.PORT, debug=SETTING.DEBUG)
