from flask import Blueprint, render_template


products_bp = Blueprint('products', __name__, template_folder='templates',
                        static_folder='static')


@products_bp.route('/')
def list():
    from models import Product
    products = Product.query.all()
    return render_template('list.html', products=products)


@products_bp.route('/details/<int:_id>')
def details(_id):
    from models import Product
    product = Product.query.filter_by(id=_id).first()
    print(product)
    return render_template('detail.html', product=product)
