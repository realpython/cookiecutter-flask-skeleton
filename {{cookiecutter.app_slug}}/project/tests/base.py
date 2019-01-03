# project/server/tests/base.py


from flask_testing import TestCase

from project.server import db, create_app
from project.server.models import User

app = create_app()


class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object("project.server.config.TestingConfig")
        return app

    def setUp(self):
        db.create_all()
        user = User(email="ad@min.com", password="admin_user")
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
