import unittest
from app import socketio, app
from models import db


class TestSocketIO(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        db.init_app(app)
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_connect(self):
        client = socketio.test_client(app)
        self.assertTrue(client.is_connected())
        client.disconnect()
        self.assertFalse(client.is_connected())

    def test_create_game(self):
        client = socketio.test_client(app)
        self.assertTrue(client.is_connected())
        received = client.get_received()
        client.emit('create:game',
                    {
                      'game_name': 'game',
                      'task_name': 'task',
                      'user_name': 'user'
                    })
        received = client.get_received()
        assert len(received[0]['args'][0]) == 2
        client.disconnect()
        self.assertFalse(client.is_connected())

    def test_get_game(self):
        client = socketio.test_client(app)
        self.assertTrue(client.is_connected())
        received = client.get_received()

        client.emit('create:game',
                    {
                      'game_name': 'game',
                      'task_name': 'task',
                      'user_name': 'user'
                    })
        uuid = client.get_received()[0]['args'][0]['game']

        client.emit('get:game',
                    {
                      'game_uuid': uuid,
                      'vote': '2',
                    })
        received = client.get_received()
        assert len(received[0]['args'][0]) == 2
        client.disconnect()
        self.assertFalse(client.is_connected())

        

