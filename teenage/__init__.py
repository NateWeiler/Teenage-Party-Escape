import os

from flask import Flask

def create_app(test_config=None):
    '''Create the app and configure it'''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'madness.sqlite')
    )

    if test_config is None:
        # load the instance config (if there is one) when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config when testing
        app.config.from_mapping(test_config)

    # make the instance folder if it doesn't exist
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # placeholder hello route
    @app.route('/')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)

    return app
