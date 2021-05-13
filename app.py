from flask import Flask
from flask_login import LoginManager
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


def init_login():
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(AdminUser).get(user_id)


if __name__ == "__main__":
    from models import db, Product, AdminUser, Order, Item
    db.init_app(app)
    init_login()
    admin_bp.add_product_view(Product, db)
    admin_bp.add_adminuser_view(AdminUser, db)
    admin_bp.add_order_view(Order, db)
    admin_bp.add_view(Item, db)
    app.run()
