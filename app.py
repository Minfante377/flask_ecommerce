from flask import Flask

import config

from products.products import products_bp
from admin.admin import AdminBluePrint


app = Flask(__name__)
app.config.from_object(config)

admin_bp = AdminBluePrint(app)
app.register_blueprint(products_bp, url_prefix='/products')
app.register_blueprint(admin_bp)

if __name__ == "__main__":
    from models import db, Product
    db.init_app(app)
    admin_bp.add_product_view(Product, db)
    app.run()
