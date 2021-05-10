from flask import Blueprint
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.form.upload import ImageUploadField


ALLOWED_IMAGE_EXTENSIONS = ['jpg', 'png', 'jpeg']
SAVE_PATH = 'products/static/'


class ProductAdminView(ModelView):

    form_columns = ['title', 'image', 'price', 'description']
    column_labels = dict(title='Titulo', image='Imagen', price='Precio',
                         description='Descripcion')

    form_overrides = {'image': ImageUploadField}
    form_args = {'image': {'base_path': SAVE_PATH,
                           'allowed_extensions': ALLOWED_IMAGE_EXTENSIONS}}


class AdminBluePrint(Blueprint):
    views = None

    def __init__(self, app):
        self.views = []
        self.admin = Admin(app)
        return super(AdminBluePrint, self).__init__('admin2', __name__,
                                                    url_prefix='/admin',
                                                    static_folder='static')

    def add_view(self, view, db):
        self.admin.add_view(ModelView(view, db.session))

    def add_product_view(self, view, db):
        self.admin.add_view(ProductAdminView(view, db.session))

    def register(self, app, options, first_registration=False):
        return super(AdminBluePrint, self).register(app, options,
                                                    first_registration)
