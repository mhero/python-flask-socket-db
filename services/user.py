from models import User, UserSchema, db
from sqlalchemy.exc import SQLAlchemyError


class UserService:

    def all():
        try:
            schema = UserSchema()
            return [schema.dump(x) for x in User.query.all()]
        except SQLAlchemyError:
            return None

    def create(socket_id, name):
        try:
            user = User(socket_id, name)
            schema = UserSchema()
            db.session.add(user)
            db.session.commit()
            return schema.dump(user)
        except SQLAlchemyError as e:
            db.session.rollback()
            error = str(e.__dict__)
            return error
