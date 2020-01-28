from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db
from services import UserService
from flask_socketio import SocketIO, emit


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
migrate = Migrate(app, db)
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(UserService.all())


@app.route('/api/users', methods=['POST'])
def create_user():
    return jsonify(UserService.create(request.json['name']))


@socketio.on('check')
def test_message(message):
    emit('up', {'data': 'got it!'})


def create_app(config_name):
    db.init_app(app)
    return app
