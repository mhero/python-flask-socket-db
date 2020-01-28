from models import User, UserSchema
from sqlalchemy.exc import SQLAlchemyError


class UserService:

    def all():
        try:
            schema = UserSchema()
            return [schema.dump(x) for x in User.query.all()]
        except SQLAlchemyError:
            return None
