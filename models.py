from app import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return self.title


db.create_all()
db.session.commit()
