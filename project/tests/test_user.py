# project/server/tests/test_user.py


import datetime
import unittest

from flask_login import current_user

from base import BaseTestCase
from project.server import bcrypt
from project.server.models import User
from project.server.user.forms import LoginForm


class TestUserBlueprint(BaseTestCase):

    def test_correct_login(self):
        # Ensure login behaves correctly with correct credentials.
        with self.client:
            response = self.client.post(
                '/login',
                data=dict(email="ad@min.com", password="admin_user"),
                follow_redirects=True
            )
            self.assertIn(b'Welcome', response.data)
            self.assertIn(b'Logout', response.data)
            self.assertIn(b'Members', response.data)
            self.assertTrue(current_user.email == "ad@min.com")
            self.assertTrue(current_user.is_active())
            self.assertEqual(response.status_code, 200)

    def test_logout_behaves_correctly(self):
        # Ensure logout behaves correctly - regarding the session.
        with self.client:
            self.client.post(
                '/login',
                data=dict(email="ad@min.com", password="admin_user"),
                follow_redirects=True
            )
            response = self.client.get('/logout', follow_redirects=True)
            self.assertIn(b'You were logged out. Bye!', response.data)
            self.assertFalse(current_user.is_active)

    def test_logout_route_requires_login(self):
        # Ensure logout route requres logged in user.
        response = self.client.get('/logout', follow_redirects=True)
        self.assertIn(b'Please log in to access this page', response.data)

    def test_member_route_requires_login(self):
        # Ensure member route requres logged in user.
        response = self.client.get('/members', follow_redirects=True)
        self.assertIn(b'Please log in to access this page', response.data)

    def test_validate_success_login_form(self):
        # Ensure correct data validates.
        form = LoginForm(email='ad@min.com', password='admin_user')
        self.assertTrue(form.validate())

    def test_validate_invalid_email_format(self):
        # Ensure invalid email format throws error.
        form = LoginForm(email='unknown', password='example')
        self.assertFalse(form.validate())

    def test_get_by_id(self):
        # Ensure id is correct for the current/logged in user.
        with self.client:
            self.client.post('/login', data=dict(
                email='ad@min.com', password='admin_user'
            ), follow_redirects=True)
            self.assertTrue(current_user.id == 1)

    def test_registered_on_defaults_to_datetime(self):
        # Ensure that registered_on is a datetime.
        with self.client:
            self.client.post('/login', data=dict(
                email='ad@min.com', password='admin_user'
            ), follow_redirects=True)
            user = User.query.filter_by(email='ad@min.com').first()
            self.assertIsInstance(user.registered_on, datetime.datetime)

    def test_check_password(self):
        # Ensure given password is correct after unhashing.
        user = User.query.filter_by(email='ad@min.com').first()
        self.assertTrue(bcrypt.check_password_hash(user.password, 'admin_user'))
        self.assertFalse(bcrypt.check_password_hash(user.password, 'foobar'))

    def test_validate_invalid_password(self):
        # Ensure user can't login when the pasword is incorrect.
        with self.client:
            response = self.client.post('/login', data=dict(
                email='ad@min.com', password='foo_bar'
            ), follow_redirects=True)
        self.assertIn(b'Invalid email and/or password.', response.data)

    def test_register_route(self):
        # Ensure about route behaves correctly.
        response = self.client.get('/register', follow_redirects=True)
        self.assertIn(b'<h1>Please Register</h1>\n', response.data)

    def test_user_registration(self):
        # Ensure registration behaves correctlys.
        with self.client:
            response = self.client.post(
                '/register',
                data=dict(email="test@tester.com", password="testing",
                          confirm="testing"),
                follow_redirects=True
            )
            self.assertIn(b'Welcome', response.data)
            self.assertTrue(current_user.email == "test@tester.com")
            self.assertTrue(current_user.is_active())
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
