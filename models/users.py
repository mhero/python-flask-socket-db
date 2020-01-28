from marshmallow import Schema, fields
from models import db


class User(db.Model):
    """
    User table
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(512))

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Object %r %r>' % (self.id, self.name)


class UserSchema(Schema):
    id = fields.Int()
    name = fields.Str()
