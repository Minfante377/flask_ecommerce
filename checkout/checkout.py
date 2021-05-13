from flask import Blueprint, render_template, session, request, abort


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


@checkout_bp.route('/order', methods=['POST'])
def order():
    from models import Item, Order, db
    items = request.json.get("items")
    print(request.json)
    if not items:
        abort(400, "No items provided")
    total = request.json.get("total")
    if total == "$0":
        abort(400, "Wrong Total")
    total = total.split("$")[1].split("<")[0]
    firstname = request.json.get("firstName")
    if not firstname:
        abort(400, "First name missing")
    lastname = request.json.get("lastName")
    if not lastname:
        abort(400, "Last name name missing")
    cellphone = request.json.get("cellphone")
    if not cellphone:
        abort(400, "Cellphone missing")
    order = Order(first_name=firstname, last_name=lastname,
                  cellphone=cellphone, total=int(total))
    db.session.add(order)
    for item in items:
        title = item['title'].split(">")[1].split("<")[0]
        db.session.add(Item(title=title, total=int(item['total'].strip("$")),
                            quantity=int(item['quantity']),
                            description=item['description'],
                            order_id=order.id))
    db.session.commit()
    return "Order created!"
