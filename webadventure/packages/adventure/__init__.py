from . import views


def init(app):
    app.register_blueprint(views.bp)
