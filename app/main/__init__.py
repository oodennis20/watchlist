from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
from flask import Blueprint
main = Blueprint('main',__name__)
from . import views,error

# APP initialization
app = Flask(__name__,instance_relative_config = True)

#  Configuration setup
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


bootstrap = Bootstrap(app)

from . import views
from . import error

def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)
    
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app