from flask import Blueprint, url_for, redirect, request, render_template
from flask_admin import Admin, AdminIndexView, expose, helpers
from flask_admin.contrib.sqla import ModelView
from flask_admin.form.upload import ImageUploadField
import flask_login as login

from wtforms import form, fields, validators
from werkzeug.security import check_password_hash, generate_password_hash


ALLOWED_IMAGE_EXTENSIONS = ['jpg', 'png', 'jpeg']
SAVE_PATH = 'products/static/'


class LoginForm(form.Form):
    username = fields.StringField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        user = self.get_user()

        if not user:
            raise validators.ValidationError('Invalid User')

        if not check_password_hash(user.password, self.password.data):
            raise validators.ValidationError('Invalid password')

    def get_user(self):
        from models import AdminUser
        return AdminUser.query.filter_by(username=self.username.data).first()


class SecureAdminIndexView(AdminIndexView):

    def is_visible(self):
        return False

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(SecureAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        form = LoginForm(request.form)

        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login.login_user(user)

        if login.current_user.is_authenticated:
            return redirect(url_for('.index'))

        return render_template('login.html', form=form)


class ProductAdminView(ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated

    form_columns = ['title', 'image', 'price', 'description', 'flavors',
                    'max_flavors']
    column_labels = dict(title='Titulo', image='Imagen', price='Precio',
                         description='Descripcion', flavors='Sabores',
                         max_flavors='Maximos sabores')

    form_overrides = {'image': ImageUploadField}
    form_args = {'image': {'base_path': SAVE_PATH,
                           'allowed_extensions': ALLOWED_IMAGE_EXTENSIONS}}


class AdminUserView(ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated

    def on_model_change(self, form, model, is_created):
        model.password = generate_password_hash(model.password)


class OrderView(ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated

    column_hide_backrefs = False
    can_view_details = True
    column_list = ('id', 'date', 'first_name', 'last_name', 'cellphone',
                   'total', 'items', 'done')
    column_labels = dict(id='ID', first_name='Nombre', last_name='Apellido',
                         cellphone='Telefono', total='Total',
                         items='Items', done="Entregada",
                         date="Fecha")


class CustomerView(ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated

    column_hide_backrefs = False
    can_view_details = True
    column_list = ('first_name', 'last_name', 'cellphone', 'orders')
    column_filters = ('first_name', 'last_name')
    column_labels = dict(first_name='Nombre', last_name='Apellido',
                         cellphone='Telefono', orders='Pedidos')


class AdminBluePrint(Blueprint):
    views = None

    def __init__(self, app):
        self.views = []
        self.admin = Admin(app, index_view=SecureAdminIndexView())
        return super(AdminBluePrint, self).__init__(
            'admin2',
            __name__,
            url_prefix='/admin',
            static_folder='static',
            template_folder='templates')

    def add_view(self, view, db):
        self.admin.add_view(ModelView(view, db.session))

    def add_product_view(self, view, db):
        self.admin.add_view(ProductAdminView(view, db.session))

    def add_adminuser_view(self, view, db):
        self.admin.add_view(AdminUserView(view, db.session))

    def add_order_view(self, view, db):
        self.admin.add_view(OrderView(view, db.session))

    def add_customer_view(self, view, db):
        self.admin.add_view(CustomerView(view, db.session))

    def register(self, app, options, first_registration=False):
        return super(AdminBluePrint, self).register(app, options,
                                                    first_registration)
