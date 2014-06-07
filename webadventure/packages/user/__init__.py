from . import models, views
from .login import login_manager


def init(app):
    # Login stuff
    login_manager.setup_app(app)
    
    # Register app blueprint
    app.register_blueprint(views.bp)
