from flask import Blueprint, request, jsonify
from app import db, redis_client
from app.models.models import Event

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def index():
    return 'OK', 200

@main_bp.route('/add', methods=['POST'])
def add():
    data = request.get_json()

    new_event = Event(
        notebook_id = data['notebook_id'],
        col_1 = data['col_1']
    )
    db.session.add(new_event)
    db.session.commit()

    return 'OK', 200

@main_bp.route('/listevents', methods=['GET'])
def list_events():
    rows = db.session.query(Event).all()

    nb_rows = len(rows)
    return jsonify(f"Number of rows : {nb_rows}"), 200

@main_bp.route('/listusers', methods=['GET'])
def list_users():
    # Retrieve the list of connected user IDs from Redis
    connected_user_ids = redis_client.smembers('connected_users')

    print('\nConnected users:\n',connected_user_ids,'\n')

    # Convert the set of user IDs to a list of strings
    connected_user_ids_str = [user_id.decode('utf-8') for user_id in connected_user_ids]

    return jsonify({'connected_users': connected_user_ids_str}), 200