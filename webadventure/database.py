from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init(app):
    db.init_app(app)


def create_all():
    # Create all tables
    db.create_all()
