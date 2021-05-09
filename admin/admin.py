from flask import Blueprint
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


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

    def register(self, app, options, first_registration=False):
        return super(AdminBluePrint, self).register(app, options,
                                                    first_registration)
