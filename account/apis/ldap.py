from base.api import BaseApi
from account.controllers import ldap as ldap_ctl


class LdapConfigApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
    }

    def post(self, request, params):
        data = ldap_ctl.get_ldap_config(**params)
        return data


class UpdateLdapConfigApi(BaseApi):

    need_params = {
        'host': ('Host', 'required str 128'),
        'admin_dn': ('管理员DN', 'required str 128'),
        'admin_password': ('管理员密码', 'required str 128'),
        'member_base_dn': ('用户基础DN', 'required str 128'),
    }
    def post(self, request, params):
        data = ldap_ctl.update_ldap_config(**params)
        return data


class SyncLdapUserApi(BaseApi):

    need_params = {
    }
    def post(self, request, params):
        data = ldap_ctl.sync_ldap_user(**params)
        return data
