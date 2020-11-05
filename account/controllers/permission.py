from django.db import transaction
from django.db.models import Q

from base import errors
from base import controllers as base_ctl
from account.models import PermissionModel
from utils.onlyone import onlyone


@onlyone.lock(PermissionModel.model_sign, 'name:sign', 'sign', 30)
@onlyone.lock(PermissionModel.model_sign, 'name', 'name', 30)
def create_permission(mod_id, name, sign, typ, rank, operator=None):
    '''
    创建权限
    '''
    obj = PermissionModel.objects.filter(name=name).first()
    if obj:
        raise errors.CommonError('权限已存在')
    obj = PermissionModel.objects.filter(sign=sign).first()
    if obj:
        raise errors.CommonError('标识已存在')
    if not PermissionModel.check_choices('typ', typ):
        raise errors.CommonError('类型值不正确')
    data = {
        'mod_id': mod_id,
        'name': name,
        'sign': sign,
        'typ': typ,
        'rank': rank,
    }
    obj = base_ctl.create_obj(PermissionModel, data, operator)
    data = obj.to_dict()
    return data


@onlyone.lock(PermissionModel.model_sign, 'obj_id:name:sign', 'sign', 30)
@onlyone.lock(PermissionModel.model_sign, 'obj_id:name', 'name', 30)
@onlyone.lock(PermissionModel.model_sign, 'obj_id', 'obj_id', 30)
def update_permission(obj_id, name, sign, typ, rank, operator=None):
    '''
    编辑权限
    '''
    obj = PermissionModel.objects.filter(name=name).exclude(id=obj_id).first()
    if obj:
        raise errors.CommonError('权限名已存在')
    obj = PermissionModel.objects.filter(sign=sign).exclude(id=obj_id).first()
    if obj:
        raise errors.CommonError('标识已存在')
    if not PermissionModel.check_choices('typ', typ):
        raise errors.CommonError('类型值不正确')

    obj = base_ctl.get_obj(PermissionModel, obj_id)
    data = {
        'name': name,
        'sign': sign,
        'typ': typ,
        'rank': rank,
    }
    obj = base_ctl.update_obj(PermissionModel, obj_id, data, operator)
    data = obj.to_dict()
    return data


@onlyone.lock(PermissionModel.model_sign, 'obj_id', 'obj_id', 30)
def delete_permission(obj_id, operator=None):
    '''
    删除权限
    '''
    base_ctl.delete_obj(PermissionModel, obj_id, operator)


def get_permissions(mod_id=None, typ=None, keyword=None, page_num=None, page_size=None, operator=None):
    '''
    获取权限列表
    '''
    base_query = PermissionModel.objects
    if mod_id:
        base_query = base_query.filter(mod_id=mod_id)
    if typ:
        base_query = base_query.filter(typ=typ)
    if keyword:
        base_query = base_query.filter(Q(name__icontains=keyword)|
                                       Q(sign__icontains=keyword))
    base_query = base_query.order_by('-rank', 'id')
    total = base_query.count()
    objs = base_ctl.query_objs_by_page(base_query, page_num, page_size)
    data_list = [obj.to_dict() for obj in objs]
    data = {
        'total': total,
        'data_list': data_list,
    }
    return data


def get_permission(obj_id, operator=None):
    '''
    获取权限信息
    '''
    obj = base_ctl.get_obj(PermissionModel, obj_id)
    data = obj.to_dict()
    return data
