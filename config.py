import os
from dotenv import load_dotenv
#connects basedir to env variables

#set abspath to config file, allows to be run on any program or OS
basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(basedir, '.env'))

class Config():
    """
    Set config variables for FLASK app,
    using environment variables. Otherwise
    create config variable it not already done
    """

    #flask uses this to store cookies
    #if secret key not found it will default to the or
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You will never guess'
    #deploy database will come from PGADMIM
    #don't let it get to sqlite!
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL') or 'sqlite' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #turn off update messages
    

