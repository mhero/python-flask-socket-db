from marshmallow import Schema, fields
from models import db, user_tasks


class User(db.Model):
    """
    User table
    """

    id = db.Column(db.String(512), primary_key=True)
    name = db.Column(db.String(512))
    user_tasks = db.relationship('Task',
                                 secondary=user_tasks, lazy='subquery',
                                 backref=db.backref('users', lazy=True)
                                 )

    def __init__(self, socket_id=None, name=None):
        self.name = name
        self.id = socket_id

    def __repr__(self):
        return '<Object %r %r>' % (self.id, self.name)


class UserSchema(Schema):
    id = fields.Str()
    name = fields.Str()
