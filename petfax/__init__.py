import os
from flask import Flask
from dotenv import load_dotenv
from flask_migrate import Migrate


def create_app():
    # configure app
    app = Flask(__name__)
    
    # load .env
    load_dotenv()
    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    from . import models
    models.db.init_app(app)
    
    migrate = Migrate(app, models.db)

    # index route
    @app.route('/')
    def index():
        return "Hello, this is PetFax!"

    # register pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)

    # register fact blueprint
    from . import fact
    app.register_blueprint(fact.bp)

    return app