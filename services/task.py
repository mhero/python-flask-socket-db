from models import Task, TaskSchema, db, Status
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
