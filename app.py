from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

from products.products import products_bp


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

app.register_blueprint(products_bp, url_prefix='/products')

if __name__ == "__main__":
    app.run()
