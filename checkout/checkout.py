from flask import Blueprint, render_template, session, request


checkout_bp = Blueprint('checkout', __name__, template_folder='templates',
                        static_folder='static')


@checkout_bp.route('/')
def make_order():
    return render_template('checkout.html',
                           products=session['session_products'])


@checkout_bp.route('/clear_product', methods=['POST'])
def clear_product():
    _id = request.json.get("_id")
    session_products = session.get('session_products', [])
    for session_product in session_products:
        if session_product.id == int(_id):
            session_products.remove(session_product)
            return "Product deleted!"
    return "No product deleted!"
