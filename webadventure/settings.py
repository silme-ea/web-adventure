# Site settings
INDEX_VIEW = 'core.index'

# Performance settings
ASSETS_DEBUG = False
ASSETS_TRACK = True

# Flask CSRF key
SECRET_KEY = '123456790'

# SQLAlchemy configuration
#SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:1@localhost/webadventure'
SQLALCHEMY_DATABASE_URI = 'sqlite:////data.sqlite'
SQLALCHEMY_ECHO = True

# Image uploads
import os.path as op
ROOT_PATH = op.join(op.dirname(__file__), 'static')

IMG_UPLOAD_URL = 'upload/img/'
IMG_UPLOAD_PATH = op.join(ROOT_PATH, 'upload', 'img')
