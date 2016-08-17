# project/server/models.py


import datetime

from project.server import app, db, bcrypt


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=True)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    last_login = db.Column(db.DateTime, nullable=False)

    def __init__(self, **kwargs):
        self.username = kwargs.get('username')
        self.email = kwargs.get('email', None)
        self.password = bcrypt.generate_password_hash(
                        kwargs.get('password'), app.config.get('BCRYPT_LOG_ROUNDS'))
        self.registered_on = datetime.datetime.now()
        self.admin = kwargs.get('admin')
        self.last_login = datetime.datetime.now()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def is_admin(self):
        return self.admin

    def __repr__(self):
        return '<User {0}>'.format(self.username)
