from flask.ext.login import current_user
from flask.ext.admin import Admin, AdminIndexView, BaseView as BaseAdminView, expose
from flask.ext.admin.contrib.sqla import ModelView

from webadventure.database import db


class AuthMixin(object):

    def is_accessible(self):
        user = current_user

        if user.is_anonymous() or not user.admin:
            return False

        return True


class BaseView(AuthMixin, BaseAdminView):
    pass


class IndexView(AuthMixin, AdminIndexView):
    pass


class BaseModelView(AuthMixin, ModelView):

    def __init__(self, model, **kwargs):
        super(BaseModelView, self).__init__(model, db.session, **kwargs)


admin = Admin(name='Adventure', index_view=IndexView())


def init(app):
    admin.init_app(app)

    original_admin_master = (admin.index_view.blueprint.jinja_loader
                             .load(app.jinja_env, 'admin/master.html'))

    @app.context_processor
    def original_admin_master_template():
        return {'original_admin_master': original_admin_master}
