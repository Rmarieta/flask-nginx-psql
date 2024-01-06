from app import db

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