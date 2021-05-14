from flask_sqlalchemy import SQLAlchemy

from app import app

db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(300), nullable=True)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(300), nullable=False)
    flavors = db.Column(db.String(200), default=[])
    max_flavors = db.Column(db.Integer, default=1)

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


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "{} {}: {}".format(self.quantity, self.title, self.description)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    cellphone = db.Column(db.String(20), nullable=False)
    total = db.Column(db.Integer, nullable=False)
    done = db.Column(db.Boolean, default=False)
    items = db.relationship('Item', backref='order')

    def __repr__(self):
        return str(self.id)


db.create_all(app=app)
db.session.commit()
