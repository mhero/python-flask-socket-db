from marshmallow import Schema, fields
from models import db, Status


class Game(db.Model):
    """
    Game table
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(512))
    status = db.Column(db.Enum(Status))
    tasks = db.relationship("Task", backref="game", lazy=True)

    def __init__(self, name=None, status=None):
        self.name = name
        self.status = status

    def __repr__(self):
        return '<Object %r %r>' % (self.id, self.name, self.status)


class GameSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    status = fields.Str()
