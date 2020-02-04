from flask import Flask, request
from flask_migrate import Migrate
from flask_cors import CORS
from models import db
from services import UserService, GameService, TaskService, UserTaskService
from flask_socketio import SocketIO, emit
import logging

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
CORS(app)
migrate = Migrate(app, db)
socketio = SocketIO(app, cors_allowed_origins="*")
logging.basicConfig(level=logging.DEBUG)


@socketio.on('create:game')
def create_game(message):
    sid = request.sid
    game = GameService.create(message['game_name'])
    task = TaskService.create(
                      message['task_name'],
                      game['id'],
                    )
    UserService.create(sid, message['user_name'])
    UserTaskService.create_or_update(task['id'],
                                     sid,
                                     0)
    emit('send:game_data', {'game': game['uuid'], 'task': task['id']})


@socketio.on('join:game')
def join_game(message):
    sid = request.sid
    UserService.create(sid, message['user_name'])


@socketio.on('get:game')
def send_message(message):
    sid = request.sid
    task = TaskService.get_active(message['game_uuid'])
    UserTaskService.create_or_update(task,
                                     sid,
                                     message['vote'])
    result = UserTaskService.get_all_users_data(task)
    emit('send:poker_data',
         {'result': result, 'game': message['game_uuid']}, broadcast=True)


def create_app(config_name):
    db.init_app(app)
    return app
