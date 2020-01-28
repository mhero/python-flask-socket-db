from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_cors import CORS
from models import db
from services import UserService, GameService, TaskService, UserTaskService
from flask_socketio import SocketIO, emit


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
CORS(app)
migrate = Migrate(app, db)
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(UserService.all())


@app.route('/api/users', methods=['POST'])
def create_user():
    return jsonify(UserService.create(request.json['name']))


@app.route('/api/games', methods=['GET'])
def get_game():
    return jsonify(GameService.all())


@app.route('/api/games', methods=['POST'])
def create_game():
    return jsonify(GameService.create(request.json['name']))


@app.route('/api/tasks', methods=['POST'])
def create_task():
    return jsonify(
                    TaskService.create(
                      request.json['name'],
                      request.json['game_id'],
                    )
                  )


@socketio.on('getPokerData')
def test_message(message):
    emit('sendPokerData', {'data': 'got it!'}, broadcast=True)


def create_app(config_name):
    db.init_app(app)
    return app
