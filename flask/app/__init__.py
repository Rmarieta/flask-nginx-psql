from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)
    
    cors = CORS(app, resources={
        r"/*": {"origins": []}
    })
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{username}:{password}@{host}:{port}/{database}'.format(
        username=os.environ['RDS_USERNAME'],
        password=os.environ['RDS_PASSWORD'],
        host=os.environ['RDS_HOSTNAME'],
        port=os.environ['RDS_PORT'],
        database=os.environ['RDS_DB_NAME'],
    )

    db.init_app(app)

    # importing and registering routes with their url prefix
    from .views.main import main_bp
    
    app.register_blueprint(main_bp, url_prefix='/')

    return app