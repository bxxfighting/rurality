from base.api import BaseApi
from account.controllers import user as user_ctl


class LoginApi(BaseApi):
    NEED_LOGIN = False

    need_params = {
        'username': ('用户名', 'required str 32'),
        'password': ('密码', 'required str 32'),
        'is_ldap': ('是否LDAP登录', 'required bool'),
    }
    def post(self, request, params):
        data = user_ctl.login(**params)
        return data


class UserApi(JsonApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('用户ID', 'required int'),
    }

    def post(self, request, params):
        data = user_ctl.get_user(**params)
        return data


class CreateUserApi(JsonApi):

    need_params = {
        'username': ('用户名', 'required str 32'),
        'password': ('密码', 'optional str 32'),
        'name': ('姓名', 'required str 32'),
        'phone': ('手机号', 'optional str 32'),
        'email': ('邮箱', 'required str 128'),
    }
    def post(self, request, params):
        data = user_ctl.create_user(**params)
        return data


class UpdateUserApi(JsonApi):

    need_params = {
        'obj_id': ('用户ID', 'required int'),
        'password': ('密码', 'optional str 32'),
        'name': ('姓名', 'required str 32'),
        'phone': ('手机号', 'optional str 32'),
        'email': ('邮箱', 'required str 128'),
    }
    def post(self, request, params):
        data = user_ctl.update_user(**params)
        return data


class DeleteUserApi(JsonApi):

    need_params = {
        'obj_id': ('用户ID', 'required int'),
    }
    def post(self, request, params):
        data = user_ctl.delete_user(**params)
        return data
