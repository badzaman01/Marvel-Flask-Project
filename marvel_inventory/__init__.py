from json import JSONDecodeError
from flask import Flask
from config import Config
#helpers import
from marvel_inventory.helpers import JSONEncoder
from .site.routes import site
from .authentication.routes import auth
from .api.routes import api
from flask_migrate import Migrate

#import models
from .models import db as root_db, login_manager, ma

#flask cors import - ross origin resource sharing
from flask_cors import CORS
app = Flask(__name__)

#pull all info from config file here
app.config.from_object(Config)

#must register blueprints to show html sites - must import site first!
app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)

root_db.init_app(app)

migrate = Migrate(app, root_db)

login_manager.init_app(app)
login_manager.login_view = 'auth.signin'

ma.init_app(app)

app.json_encoder = JSONEncoder

CORS(app)