from flask import Flask, redirect, url_for
from flask_session import Session

import config

from products.products import products_bp
from checkout.checkout import checkout_bp
from admin.admin import AdminBluePrint


app = Flask(__name__)
app.config.from_object(config)

Session(app)

admin_bp = AdminBluePrint(app)
app.register_blueprint(products_bp, url_prefix='/products')
app.register_blueprint(checkout_bp, url_prefix='/checkout')
app.register_blueprint(admin_bp)


@app.route("/", methods=['GET'])
def home():
    return redirect(url_for("products.list"))
