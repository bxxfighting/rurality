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


class LogoutApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
    }
    def post(self, request, params):
        # TODO: 如果token写入了redis，可以在这里清除
        pass


class UserApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('用户ID', 'required int'),
    }

    def post(self, request, params):
        data = user_ctl.get_user(**params)
        return data


class CreateUserApi(BaseApi):

    need_params = {
        'username': ('用户名', 'required str 32'),
        'password': ('密码', 'optional str 32'),
        'name': ('姓名', 'required str 32'),
        'phone': ('手机号', 'optional str 32'),
        'email': ('邮箱', 'optional str 128'),
    }
    def post(self, request, params):
        data = user_ctl.create_user(**params)
        return data


class UpdateUserApi(BaseApi):

    need_params = {
        'obj_id': ('用户ID', 'required int'),
        'password': ('密码', 'optional str 32'),
        'name': ('姓名', 'required str 32'),
        'phone': ('手机号', 'optional str 32'),
        'email': ('邮箱', 'optional str 128'),
    }
    def post(self, request, params):
        data = user_ctl.update_user(**params)
        return data


class DeleteUserApi(BaseApi):

    need_params = {
        'obj_id': ('用户ID', 'required int'),
    }
    def post(self, request, params):
        data = user_ctl.delete_user(**params)
        return data


class ListUserApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'keyword': ('关键词', 'optional str 16'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = user_ctl.get_users(**params)
        return data


class CurrentUserApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
    }
    def post(self, request, params):
        params['obj_id'] = request.user_id
        data = user_ctl.get_user_info(**params)
        return data


class ListUserRoleApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('用户ID', 'required int'),
    }
    def post(self, request, params):
        data = user_ctl.get_roles_by_user_id(**params)
        return data


class ListUserDepartmentApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('用户ID', 'required int'),
    }
    def post(self, request, params):
        data = user_ctl.get_departments_by_user_id(**params)
        return data
