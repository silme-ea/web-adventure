from . import views


def init(app):
    # Register app blueprint
    app.register_blueprint(views.bp)
