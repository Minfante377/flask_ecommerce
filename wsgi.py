from app import app, admin_bp

from flask_login import LoginManager

import os


def init_login():
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(AdminUser).get(user_id)


if __name__ == "__main__":
    from models import db, Product, AdminUser, Order, Customer
    db.init_app(app)
    init_login()
    admin_bp.add_product_view(Product, db)
    admin_bp.add_adminuser_view(AdminUser, db)
    admin_bp.add_order_view(Order, db)
    admin_bp.add_customer_view(Customer, db)
    app.run(port=int(os.environ.get("PORT", 5000)), host="0.0.0.0")
