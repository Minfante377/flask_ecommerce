from flask import Blueprint, render_template, session, request, abort


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


@products_bp.route('/add_product', methods=['POST'])
def add_product():
    from models import Product
    _id = request.json.get('_id')
    product = Product.query.filter_by(id=_id).first()
    session_products = session.get('session_products', [])
    for session_product in session_products:
        if not product or product.id == session_product.id:
            abort(400, "No product added")
    if 'session_products' in session:
        session['session_products'].append(product)
    else:
        session['session_products'] = []
        session['session_products'].append(product)
    return "Product added correctly: {}".format(product)
