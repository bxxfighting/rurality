from django.db import transaction
from django.db.models import Q

from base import errors
from base import controllers as base_ctl
from account.models import DepartmentModel


def create_department(name, sign, operator=None):
    '''
    创建部门
    '''
    if DepartmentModel.objects.filter(name=name).exists():
        raise errors.CommonError('部门名称已存在')
    if DepartmentModel.objects.filter(sign=sign).exists():
        raise errors.CommonError('部门标识已存在')
    data = {
        'name': name,
        'sign': sign,
    }
    obj = base_ctl.create_obj(DepartmentModel, data, operator)
    data = obj.to_dict()
    return data


def update_department(obj_id, name, sign, operator=None):
    '''
    编辑部门
    '''
    if DepartmentModel.objects.filter(name=name).exclude(id=obj_id).exists():
        raise errors.CommonError('部门名称已存在')
    if DepartmentModel.objects.filter(sign=sign).exclude(id=obj_id).exists():
        raise errors.CommonError('部门标识已存在')
    obj = base_ctl.get_obj(DepartmentModel, obj_id)
    data = {
        'name': name,
        'sign': sign,
    }
    obj = base_ctl.update_obj(DepartmentModel, obj_id, data, operator)
    data = obj.to_dict()
    return data


def delete_department(obj_id, operator=None):
    '''
    删除部门
    '''
    obj = base_ctl.get_obj(DepartmentModel, obj_id)
    base_ctl.delete_obj(DepartmentModel, obj_id, operator)


def get_departments(keyword=None, page_num=None, page_size=None, operator=None):
    '''
    获取部门列表
    '''
    base_query = DepartmentModel.objects
    if keyword:
        base_query = base_query.filter(Q(name__icontains=keyword)|
                                       Q(sign__icontains=keyword))
    total = base_query.count()
    objs = base_ctl.query_objs_by_page(base_query, page_num, page_size)
    data_list = [obj.to_dict() for obj in objs]
    for obj in objs:
        data = obj.to_dict()
        data_list.append(data)
    data = {
        'total': total,
        'data_list': data_list,
    }
    return data


def get_department(obj_id, operator=None):
    '''
    获取部门信息
    '''
    obj = base_ctl.get_obj(DepartmentModel, obj_id)
    data = obj.to_dict()
    return data
