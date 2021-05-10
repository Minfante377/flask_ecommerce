import os


PWD = os.path.abspath(os.curdir)
DEBUG = True

# Security
SECRET_KEY = 'SUPER SECRET KEY'

# Database
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD)
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Admin
FLASK_ADMIN_SWATCH = 'cerulean'
UPLOAD_FOLDER = 'products/static/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
