# flake8: noqa
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from models.users import User, UserSchema
