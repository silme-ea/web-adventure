# Flask CSRF key
SECRET_KEY = '123456790'

# Google maps key
GOOGLE_MAPS_KEY = 'AIzaSyD6ZKQ2MRcTtPnOHd71yHUljeaj1sNLcKM'

# SQLAlchemy configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///../data.sqlite'
#SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:1@localhost/tvcb'
SQLALCHEMY_ECHO = True

# Site settings
INDEX_VIEW = 'site.home'

# Recaptcha
RECAPTCHA_USE_SSL = True
RECAPTCHA_PUBLIC_KEY = '6Ld77N0SAAAAAG-C3i3Oab5HkWdezs5t9gCYQDy4'
RECAPTCHA_PRIVATE_KEY = '6Ld77N0SAAAAAD-OOp7rIRofPkrxeKG2iaOkhXtP'

# Google
GOOGLE_APP_KEY = '334068587572.apps.googleusercontent.com'
GOOGLE_APP_SECRET = 'XQn51w4IASyod3cWTaDFmKGd'

# Image uploads
import os.path as op
ROOT_PATH = op.join(op.dirname(__file__), 'static')

IMG_UPLOAD_URL = 'upload/img/'
IMG_UPLOAD_PATH = op.join(ROOT_PATH, 'upload', 'img')
