from flask_sqlalchemy import SQLAlchemy

from app import app

db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(300), nullable=True)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return self.title


class AdminUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    cellphone = db.Column(db.String(20))
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(64))

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __unicode__(self):
        return self.username


db.create_all(app=app)
db.session.commit()
