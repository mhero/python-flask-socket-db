from marshmallow import Schema, fields
from models import db, Status
import uuid


class Game(db.Model):
    """
    Game table
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(512))
    status = db.Column(db.Enum(Status))
    uuid = db.Column(db.String(512))
    tasks = db.relationship("Task", backref="game", lazy=True)

    def __init__(self, name=None, status=None):
        self.name = name
        self.status = status
        self.uuid = str(uuid.uuid4())

    def __repr__(self):
        return '<Object %r %r>' % (self.id, self.name, self.status, self.uuid)


class GameSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    status = fields.Str()
    uuid = fields.Str()
