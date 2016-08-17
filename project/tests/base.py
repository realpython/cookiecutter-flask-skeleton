# project/server/tests/base.py


from flask_testing import TestCase

from project.server import app, db
from project.server.models import User


class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('project.server.config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()
        user = User(username="ad@min", password="admin_user", admin=True)
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
