from flask.ext.login import LoginManager

from webadventure.database import db

from .models import User

login_manager = LoginManager()


@login_manager.user_loader
def load_user(userid):
    return db.session.query(User).get(userid)

login_manager.login_view = "user.login_view"
