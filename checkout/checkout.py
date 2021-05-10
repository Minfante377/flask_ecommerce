from flask import Blueprint, render_template


checkout_bp = Blueprint('checkout', __name__, template_folder='templates',
                        static_folder='static')


@checkout_bp.route('/')
def make_order():
    from models import Product
    products = Product.query.all()
    return render_template('checkout.html', products=products)
