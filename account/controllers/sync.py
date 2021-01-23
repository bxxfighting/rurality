from django.db import transaction
from django.db.models import Q

from account.models import UserModel
from account.models import LdapConfigModel
from base import controllers as base_ctl
from base import errors
from utils.ldap_cli import LdapCli


def sync_ldap_user():
    '''
    同步LDAP用户
    '''
    config_obj = LdapConfigModel.objects.first()
    if not config_obj:
        raise errors.CommonError('请先配置LDAP参数')
    data = {
        'host': config_obj.host,
        'member_base_dn': config_obj.member_base_dn,
        'admin_dn': config_obj.admin_dn,
        'admin_password': config_obj.admin_password,
    }
    ldap_cli = LdapCli(**data)
    users = ldap_cli.get_users()
    query = {
        'status': UserModel.ST_NORMAL,
        'typ': UserModel.TYP_LDAP,
    }
    old_ids = UserModel.objects.filter(**query).values_list('id', flat=True).all()
    old_ids = list(set(old_ids))
    existed_ids = []
    data_list = []
    for user in users:
        username = user.get('username')
        name = user.get('name')
        query = {
            'username': username,
            'typ': UserModel.TYP_LDAP,
        }
        obj = UserModel.objects.filter(**query).first()
        if not obj:
            data = query
            data['name'] = name
            data_list.append(data)
        else:
            existed_ids.append(obj.id)
    base_ctl.create_objs(UserModel, data_list)
    deleted_ids = list(set(set(old_ids) - set(existed_ids)))
    if deleted_ids:
        UserModel.objects.filter(id__in=deleted_ids).update(status=UserModel.ST_FORBIDDEN)
