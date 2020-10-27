from django.db import transaction
from django.db.models import Q

from base import errors
from base import controllers as base_ctl
from account.models import RoleModel


def create_role(name, sign, operator=None):
    '''
    创建角色
    '''
    obj = RoleModel.objects.filter(name=name).first()
    if obj:
        raise errors.CommonError('角色已存在')
    obj = RoleModel.objects.filter(sign=sign).first()
    if obj:
        raise errors.CommonError('标识已存在')
    data = {
        'name': name,
        'sign': sign,
    }
    obj = base_ctl.create_obj(RoleModel, data, operator)
    data = obj.to_dict()
    return data


def update_role(obj_id, name, sign, operator=None):
    '''
    编辑角色
    '''
    obj = RoleModel.objects.filter(name=name).exclude(id=obj_id).first()
    if obj:
        raise errors.CommonError('角色名已存在')
    obj = RoleModel.objects.filter(sign=sign).exclude(id=obj_id).first()
    if obj:
        raise errors.CommonError('标识已存在')

    obj = base_ctl.get_obj_or_none(RoleModel, obj_id)
    if not obj:
        raise errors.CommonError('角色不存在')
    if obj.sign == 'admin':
        raise errors.CommonError('超级管理员不允许编辑')
    data = {
        'name': name,
        'sign': sign,
    }
    obj = base_ctl.update_obj(RoleModel, obj_id, data, operator)
    data = obj.to_dict()
    return data


def delete_role(obj_id, operator=None):
    '''
    删除角色
    '''
    obj = base_ctl.get_obj_or_none(RoleModel, obj_id)
    if not obj:
        raise errors.CommonError('角色不存在')
    if obj.sign == 'admin':
        raise errors.CommonError('超级管理员不允许删除')
    base_ctl.delete_obj(RoleModel, obj_id, operator)


def get_roles(keyword=None, page_num=None, page_size=None, operator=None):
    '''
    获取角色列表
    '''
    base_query = RoleModel.objects
    if keyword:
        base_query = base_query.filter(Q(name__icontains=keyword)|
                                       Q(sign__icontains=keyword))
    total = base_query.count()
    objs = base_ctl.query_objs_by_page(base_query, page_num, page_size)
    data_list = [obj.to_dict() for obj in objs]
    data = {
        'total': total,
        'data_list': data_list,
    }
    return data


def get_role(obj_id, operator=None):
    '''
    获取角色信息
    '''
    obj = base_ctl.get_obj(RoleModel, obj_id)
    data = obj.to_dict()
    return data
