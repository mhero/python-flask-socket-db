from models import Game, GameSchema, db, Status
from sqlalchemy.exc import SQLAlchemyError


class GameService:

    def all():
        try:
            schema = GameSchema()
            return [schema.dump(x) for x in Game.query.all()]
        except SQLAlchemyError:
            return None

    def create(name):
        try:
            game = Game(name, Status.active)
            schema = GameSchema()
            db.session.add(game)
            db.session.commit()
            return schema.dump(game)
        except SQLAlchemyError as e:
            error = str(e.__dict__)
            return error
