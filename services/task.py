from models import Task, TaskSchema, db, Status, Game
from sqlalchemy.exc import SQLAlchemyError


class TaskService:

    def create(name, game_id):
        try:
            task = Task(name, Status.active, game_id)
            schema = TaskSchema()
            db.session.add(task)
            db.session.commit()
            return schema.dump(task)
        except SQLAlchemyError as e:
            error = str(e.__dict__)
            return error

    def get_active(game_id):
        try:
            return db.session.query(Task.id, Task.name).\
                        join(Game, Task.id == Game.id).\
                        filter(Task.status == Status.active).\
                        filter(Game.id == game_id).first()[0]
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            return error
