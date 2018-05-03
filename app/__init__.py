# -*- coding: utf-8 -*-
"""Flask project init."""


from flask import Flask
from flask.cli import AppGroup
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config

db = SQLAlchemy()
bootstrap = Bootstrap()
moment = Moment()
migrate = Migrate()


def create_app(config_name):
    """Create app."""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    # group commands
    command_group_cli = AppGroup('command_group')
    app.cli.add_command(command_group_cli)

    db.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    migrate.init_app(app, db)

    # import blueprint
    from .errors import errors as errors_blueprint
    app.register_blueprint(errors_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
