from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS


# Global plugins
db = SQLAlchemy()
ma = Marshmallow()

def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    ma.init_app(app)
    CORS(app) 

    with app.app_context():
        # Include our Routes
        from .controllers import usersController, testsController

        #init db
        db.create_all()
        db.session.commit()

        # Register Blueprints
        app.register_blueprint(usersController.users_bp)
        app.register_blueprint(testsController.tests_bp)
        
        
        return app