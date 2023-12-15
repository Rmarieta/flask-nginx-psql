from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os 

db = SQLAlchemy()

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://psql:pswd@db-test:5432/db'

db.init_app(application)

class EventParent(db.Model):

    __tablename__ = 'EventParent'

    id = db.Column(db.Integer, primary_key=True)
    notebook_id = db.Column(db.String(100), nullable=False)
    event_type = db.Column(db.String(32), nullable=False)
    __mapper_args__ = {
        'polymorphic_identity': 'EventParent',
        'polymorphic_on': event_type
    }

class Event(EventParent):

    __tablename__ = 'Event'

    id = db.Column(db.Integer, db.ForeignKey('EventParent.id'), primary_key=True)
    col_1 = db.Column(db.String(200), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'Event'
    }

nb_entries = 50000
notebook_id = 'postman_python'
content = "wngfiwrhguirehgiuerhgiuthiuthbirubntruituihthbrtwngfiwrhguirehgiuerhgiuthiuthbirubntruituihthbrtwngfiwrhguirehgiuerhgiuthiuthbirubntruituihthbrtwngfiwrhguirehgiuerhgiuthiuthbirubntruituihthbrtwng"

with application.app_context():
    db.create_all()
    # populate the table
    if Event.query.first() is None :
        for n in range(nb_entries) :
            new_event = Event(
                notebook_id=notebook_id,
                col_1=content
            )

            db.session.add(new_event)
            db.session.commit()
    
    db.session.close()

@application.route('/listevents', methods=['GET'])
def list_events():
    rows = db.session.query(Event).all()

    nb_rows = len(rows)
    return jsonify(f"Number of rows : {nb_rows}"), 200


if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0")