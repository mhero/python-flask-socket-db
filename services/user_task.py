from models import db, user_tasks, User, Task
from sqlalchemy.exc import SQLAlchemyError


class UserTaskService:

    def record_exists(task_id, user_id):
        try:
            return db.session.query(user_tasks).filter_by(
                                        task_id=task_id,
                                        user_id=user_id
                                        ).count()
        except SQLAlchemyError as e:
            error = str(e.__dict__)
            return error

    def create(task_id, user_id, value):
        try:
            statement = user_tasks.insert().values(
                                                    task_id=task_id, 
                                                    user_id=user_id,
                                                    value=value
                                                    )
            db.session.execute(statement)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            error = str(e.__dict__)
            return error

    def update(task_id, user_id, value):
        try:
            statement = user_tasks.update().\
                                   values(value=value).\
                                   where(user_tasks.c.task_id == task_id).\
                                   where(user_tasks.c.user_id == user_id)
            db.session.execute(statement)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            error = str(e.__dict__)
            return error
    
    def create_or_update(task_id, user_id, value):
        count = UserTaskService.record_exists(task_id, user_id)
        if count >= 1:
            UserTaskService.update(task_id, user_id, value)
        else:
            UserTaskService.create(task_id, user_id, value)

    def get_all_users_data(task_id):
        try:
            return db.session.query(User.id, User.name, user_tasks.c.value).\
                            join(user_tasks, user_tasks.c.user_id == User.id).\
                            filter(user_tasks.c.task_id == task_id).\
                            join(Task, Task.id == user_tasks.c.task_id).all()
        except SQLAlchemyError as e:
            error = str(e.__dict__)
            return error
