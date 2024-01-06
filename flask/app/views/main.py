from flask import Blueprint, request, jsonify
from app import db
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