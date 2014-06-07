from webadventure.database import db

from .models import User
from .tools import encrypt_password


# Various model-related api
def get_user(username):
    return db.session.query(User).filter_by(username=username).first()


def user_exists(username):
    return db.session.query(User).filter_by(username=username).count() > 0


def create_user(username, password=None):
    user = User()
    user.username = username
    user.active = False

    if password:
        user.password = encrypt_password(password)

    return user


def create_external_user(username, external):
    user = create_user(username)
    user.external = external
    user.active = True

    return user


def change_password(user, password):
    user.password = encrypt_password(password)
    return user
