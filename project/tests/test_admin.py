import datetime
import unittest

from flask_login import current_user

from base import BaseTestCase
from project.server import bcrypt
from project.server.models import User
from project.server.user.forms import LoginForm


class TestAdminBlueprint(BaseTestCase):

    def test_check_password(self):
        # Ensure given password is correct after unhashing.
        user = User.query.filter_by(username='ad@min').first()
        self.assertTrue(bcrypt.check_password_hash(user.password, 'admin_user'))
        self.assertFalse(bcrypt.check_password_hash(user.password, 'foobar'))

    def test_validate_success_login_form(self):
        # Ensure correct data validates.
        form = LoginForm(username='ad@min', password='admin_user')
        self.assertTrue(form.validate())

    def test_validate_invalid_password(self):
        # Ensure user can't login when the password is incorrect.
        with self.client:
            response = self.client.post('/admin/', data=dict(
                username='ad@min', password='foo_bar'
            ), follow_redirects=True)
        self.assertIn(b'Invalid username and/or password.', response.data)


if __name__ == '__main__':
    unittest.main()
