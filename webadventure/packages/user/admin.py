from webadventure.admin import BaseModelView

from . import models


class UserAdmin(BaseModelView):
    can_create = False

    column_exclude_list = ('password',)

    form_columns = ('username', 'admin', 'active')

    column_searchable_list = ('username', )

    column_filters = ('username', )

    def __init__(self):
        super(UserAdmin, self).__init__(models.User,
                                        name='List',
                                        category='Users')
