from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_socketio import SocketIO
import os

db = SQLAlchemy()
socketio = SocketIO()

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
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

    db.init_app(app)
    socketio.init_app(app, message_queue='redis://redis')

    # importing and registering routes with their url prefix
    from .views.main import main_bp
    
    app.register_blueprint(main_bp, url_prefix='/')

    return app