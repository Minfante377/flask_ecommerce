from flask import Blueprint, render_template


products_bp = Blueprint('products', __name__, template_folder='templates',
                        static_folder='static')


@products_bp.route('/')
def list():
    from models import Product
    products = Product.query.all()
    return render_template('list.html', products=products)
