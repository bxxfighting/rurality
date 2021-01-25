from django.db import transaction
from django.db.models import Q

from base import errors
from base import controllers as base_ctl
from account.models import LdapConfigModel
from scheduler.controllers import berry as berry_ctl
from account.controllers import user as user_ctl
from utils.onlyone import onlyone


def get_ldap_config(operator=None):
    '''
    获取LDAP配置信息
    '''
    obj = LdapConfigModel.objects.first()
    has_password = False
    if operator and user_ctl.has_permission(operator.id, LdapConfigModel.PASSWORD_PERMISSION):
        has_password = True
    if obj:
        data = obj.to_dict(has_password=has_password)
    else:
        data = LdapConfigModel.none_to_dict()
    return data


@onlyone.lock(LdapConfigModel.model_sign, '', '', 30)
def update_ldap_config(host, admin_dn, admin_password, member_base_dn, operator=None):
    '''
    编辑服务配置
    '''
    # TODO: 这里应该增加校验ldap参数对不对的逻辑，但是我有点不会
    obj = LdapConfigModel.objects.first()
    data = {
        'host': host,
        'admin_dn': admin_dn,
        'admin_password': admin_password,
        'member_base_dn': member_base_dn,
    }
    if obj:
        obj = base_ctl.update_obj(LdapConfigModel, obj.id, data, operator)
    else:
        obj = base_ctl.create_obj(LdapConfigModel, data, operator)
    data = obj.to_dict()
    return data


def sync_ldap_user(operator=None):
    '''
    同步用户
    '''
    config_obj = LdapConfigModel.objects.first()
    if not config_obj:
        raise errors.CommonError('请先配置LDAP参数')
    params = {}
    data = {
        'name': '同步LDAP用户',
        'typ': 'sync_ldap_user',
        'params': params,
    }
    berry_ctl.create_berry(**data)
