from django.db import transaction
from django.db.models import Q

from base import errors
from base import controllers as base_ctl
from account.models import DepartmentModel
from account.models import DepartmentUserModel
from utils.onlyone import onlyone


@onlyone.lock(DepartmentModel.model_sign, 'name:sign', 'sign', 30)
@onlyone.lock(DepartmentModel.model_sign, 'name', 'name', 30)
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


@onlyone.lock(DepartmentModel.model_sign, 'obj_id:name:sign', 'sign', 30)
@onlyone.lock(DepartmentModel.model_sign, 'obj_id:name', 'name', 30)
@onlyone.lock(DepartmentModel.model_sign, 'obj_id', 'obj_id', 30)
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


@onlyone.lock(DepartmentModel.model_sign, 'obj_id', 'obj_id', 30)
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


@onlyone.lock(DepartmentUserModel.model_sign, 'department_id:user_id', 'department_id:user_id', 30)
def create_department_user(department_id, user_id, typ, operator=None):
    '''
    创建部门关联用户
    '''
    query = {
        'user_id': user_id,
        'department_id': department_id,
    }
    if DepartmentUserModel.objects.filter(**query).exists():
        raise errors.CommonError('用户已在此部门中')
    if not DepartmentUserModel.check_choices('typ', typ):
        raise errors.CommonError('类型值不正确')
    data = {
        'user_id': user_id,
        'department_id': department_id,
        'typ': typ,
    }
    obj = base_ctl.create_obj(DepartmentUserModel, data, operator)
    data = obj.to_dict()
    return data


@onlyone.lock(DepartmentUserModel.model_sign, 'department_id:user_id', 'department_id:user_id', 30)
def update_department_user(department_id, user_id, typ, operator=None):
    '''
    编辑部门关联用户
    '''
    query = {
        'user_id': user_id,
        'department_id': department_id,
    }
    obj = DepartmentUserModel.objects.filter(**query).first()
    if not obj:
        raise errors.CommonError('用户未在此部门')
    if not DepartmentUserModel.check_choices('typ', typ):
        raise errors.CommonError('类型值不正确')
    data = {
        'typ': typ,
    }
    obj = base_ctl.update_obj(DepartmentUserModel, obj.id, data, operator)
    data = obj.to_dict()
    return data


@onlyone.lock(DepartmentUserModel.model_sign, 'department_id:user_id', 'department_id:user_id', 30)
def delete_department_user(department_id, user_id, operator=None):
    '''
    删除部门关联用户
    '''
    query = {
        'user_id': user_id,
        'department_id': department_id,
    }
    obj = DepartmentUserModel.objects.filter(**query).first()
    if not obj:
        raise errors.CommonError('用户未在此部门中')
    base_ctl.delete_obj(DepartmentUserModel, obj.id, operator)


def get_department_users(obj_id, typ=None, page_num=None, page_size=None, operator=None):
    '''
    获取部门用户列表
    '''
    base_query = DepartmentUserModel.objects.filter(department_id=obj_id)\
            .filter(user__is_deleted=False).select_related('user')
    if typ:
        base_query = base_query.filter(typ=typ)
    total = base_query.count()
    objs = base_ctl.query_objs_by_page(base_query, page_num, page_size)
    data_list = []
    for obj in objs:
        data = obj.to_dict()
        data['user'] = obj.user.to_dict()
        data_list.append(data)
    data = {
        'total': total,
        'data_list': data_list,
    }
    return data


def get_department_ids_by_user_id(user_id, operator=None):
    '''
    获取用户关联的部门ID列表
    '''
    ids = DepartmentUserModel.objects.filter(user_id=user_id)\
            .values_list('department_id', flat=True).all()
    return list(set(ids))


def get_departments_by_ids(obj_ids, operator=None):
    '''
    根据部门ID列表获取部门列表
    '''
    objs = DepartmentModel.objects.filter(id__in=obj_ids).all()
    data_list = [obj.to_dict() for obj in objs]
    return data_list
