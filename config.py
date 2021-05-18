import os


PWD = os.path.abspath(os.curdir)
DEBUG = False

# Security
SECRET_KEY = 'SUPER SECRET KEY'

# Database
if DEBUG:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD)
else:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').\
        replace("postgres", "postgresql")
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Admin
FLASK_ADMIN_SWATCH = 'cerulean'
UPLOAD_FOLDER = 'products/static/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

# Session
SESSION_TYPE = 'filesystem'
