from gevent import monkey
monkey.patch_all()

from flask import Flask, jsonify
from app import create_app, db, socketio

application = create_app()

import os
HOSTNAME = os.uname().nodename

@application.route('/hostname')
def get_hostname():
    return jsonify({'hostname': HOSTNAME})

if __name__ == "__main__":
    socketio.run(application, debug=True, host='0.0.0.0')