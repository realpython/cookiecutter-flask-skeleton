# project/server/user/forms.py


from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email

from project.server import db
from project.server.models import User


class LoginForm(Form):
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])

    def get_user(self):
        return db.session.query(User).filter_by(username=self.username.data).first()


class RegisterForm(Form):
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=3, max=40)])
    email = StringField('Email',validators=[DataRequired(), Email(message=None), Length(min=6, max=40)])
    password = PasswordField('Password',
                            validators=[DataRequired(), Length(min=6, max=25)])
    confirm = PasswordField('Confirm password', validators=[DataRequired(),
                    EqualTo('password', message='Passwords must match.')])
