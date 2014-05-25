import os.path as op

from flask import Flask

# Application
app = Flask(__name__)


def init(settings):
    # Load configuration
    app.config.from_object(settings)

    # Configure modules
    from filmtemecula import database, admin

    database.init(app)
    admin.init(app)

    # Import packages
    from filmtemecula import packages

    # Initialize packages
    packages.user.init(app)
    packages.site.init(app)
    packages.survey.init(app)
    packages.location.init(app)
