from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Teams, Players

class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        # Will be called before every test
        db.create_all()
        db.session.add(Players(description="Run unit tests"))
        db.session.commit()

    def tearDown(self):
        # Will be called after every test
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    # Test whether we get a successful response from our routes
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)
    
    def test_create_player_get(self):
        response = self.client.get(url_for('create_player'))
        self.assert200(response)

    def test_read_players_get(self):
        response = self.client.get(url_for('read_players'))
        self.assert200(response)

    def test_update_player_get(self):
        response = self.client.get(url_for('update_player', id=1))
        self.assert200(response)

class TestRead(TestBase):

    def test_read_home_players(self):
        response = self.client.get(url_for('home'))
        self.assertIn(b"Run unit tests", response.data)
    
    def test_read_players_dictionary(self):
        response = self.client.get(url_for('read_players'))
        self.assertIn(b"Run unit tests", response.data)

class TestCreate(TestBase):

    def test_create_player(self):
        response = self.client.post(
            url_for('create_player'),
            data={"description": "Testing create functionality"},
            follow_redirects=True
        )
        self.assertIn(b"Testing create functionality", response.data)
    
class TestUpdate(TestBase):

    def test_update_player(self):
        response = self.client.post(
            url_for('update_player', id=1),
            data={"description": "Testing update functionality"},
            follow_redirects=True
        )
        self.assertIn(b"Testing update functionality", response.data)
    
    def test_complete_player(self):
        response = self.client.get(url_for('complete_player', id=1), follow_redirects=True)
        self.assertEqual(Players.query.get(1).completed, True)
    
        

class TestDelete(TestBase):

    def test_delete_player(self):
        response = self.client.get(
            url_for('delete_player', id=1),
            follow_redirects=True
        )
        self.assertNotIn(b"Run unit tests", response.data)
