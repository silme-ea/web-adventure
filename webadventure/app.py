from flask import Flask

# Application
app = Flask(__name__)


def init(settings):
    # Load configuration
    app.config.from_object(settings)

    # Configure modules
    from webadventure import database, admin, assets

    database.init(app)
    admin.init(app)
    assets.init(app)

    # Import packages
    from webadventure import packages

    # Initialize packages
    packages.core.init(app)
    packages.user.init(app)
    packages.adventure.init(app)
