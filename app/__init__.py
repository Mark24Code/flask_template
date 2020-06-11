from flask import Flask, render_template
from config import config
from flask_cors import CORS


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)

    # extensions
    CORS(app)

    # register blueprints
    from .welcome import welcome as welcome_blueprint
    app.register_blueprint(welcome_blueprint)
    
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    # others
    if config_name == 'development' or 'default':
        print('----routes---')
        print(app.url_map)
        print('-------------')

    return app
