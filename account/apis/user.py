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
