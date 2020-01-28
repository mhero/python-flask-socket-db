# flake8: noqa
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

user_tasks = db.Table('user_tasks',
    db.Column('task_id', db.Integer, db.ForeignKey('task.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)

from models.status import Status
from models.users import User, UserSchema
from models.tasks import Task, TaskSchema
from models.games import Game, GameSchema

