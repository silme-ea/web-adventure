from webadventure.database import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(128), unique=True, index=True)
    password = db.Column(db.String(64))

    # Flags
    admin = db.Column(db.Boolean(), default=False)
    active = db.Column(db.Boolean(), default=True)

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __unicode__(self):
        return self.username
