from marshmallow import Schema, fields
from models import db, Status


class Task(db.Model):
    """
    Task table
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(512))
    status = db.Column(db.Enum(Status))
    game_id = db.Column(db.Integer,
                        db.ForeignKey('game.id'),
                        nullable=False)

    def __init__(self, name=None, status=None, game_id=None):
        self.name = name
        self.status = status
        self.game_id = game_id

    def __repr__(self):
        return '<Object %r %r>' % (self.id, self.name, self.status)


class TaskSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    status = fields.Str()
    game_id = fields.Int()
