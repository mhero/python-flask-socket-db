from models import db, User, Task
from sqlalchemy.exc import SQLAlchemyError


class UserTaskService:

    def create(user_id, task_id):
        try:
            user = User.query.get(user_id)
            task = Task.query.get(task_id)
            user.user_tasks.append(task)
            db.session.add(user)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            error = str(e.__dict__)
            return error
