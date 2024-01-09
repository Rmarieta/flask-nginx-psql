import eventlet  

# perform monkey patching for eventlet
eventlet.monkey_patch()

from flask import Flask, jsonify
from app import create_app, db, socketio
from flask.cli import FlaskGroup

application = create_app()
cli = FlaskGroup(application)

# define that to create the tables having access to the app context from the container shell
@cli.command('create_all')
def create_all():
    with application.app_context():
        db.create_all()

import os
HOSTNAME = os.uname().nodename

@application.route('/hostname')
def get_hostname():
    return jsonify({'hostname': HOSTNAME})

if __name__ == "__main__":
    cli()
    # socketio.run(application, debug=True, host='0.0.0.0')