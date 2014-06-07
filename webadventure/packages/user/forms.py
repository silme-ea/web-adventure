from flask.ext import wtf
from wtforms import validators, widgets
from wtforms.fields import StringField, PasswordField

from .api import user_exists, create_user, get_user
from .tools import verify_password


class RegisterForm(wtf.Form):
    email = StringField('Email',
                        validators=[validators.Required()])
    password = PasswordField('Password', validators=[validators.Required()])
    password2 = PasswordField('Confirm', validators=[validators.Required()])

    def validate_password(self, field):
        if self.password.data != self.password2.data:
            raise validators.ValidationError('Passwords don\'t match!')

    def validate_email(self, field):
        if user_exists(self.email.data):
            raise validators.ValidationError('User already exists')

    def get_user(self):
        user = create_user(self.email.data, self.password.data)
        return user


class LoginForm(wtf.Form):
    email = StringField('Email',
                        validators=[validators.Required()],
                        widget=widgets.Input(input_type='email'))
    password = PasswordField('Password', validators=[validators.Required()])

    def __init__(self, form):
        super(LoginForm, self).__init__(form)

        self.cached_user = None

    def validate_email(self, field):
        self.cached_user = get_user(self.email.data)

        if self.cached_user is None:
            raise validators.ValidationError('Invalid user or password')

        if not verify_password(self.cached_user, self.password.data):
            raise validators.ValidationError('Invalid user or password')

        if not self.cached_user.active:
            raise validators.ValidationError('Please activate your account')

    def validate_password(self, field):
        self.cached_user = get_user(self.email.data)

        if self.cached_user is None:
            raise validators.ValidationError('Invalid user or password')

        if not verify_password(self.cached_user, self.password.data):
            raise validators.ValidationError('Invalid user or password')
