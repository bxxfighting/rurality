from django.db import transaction
from django.db.models import Q

from base import errors
from base import controllers as base_ctl
from account.models import RoleModel
from account.models import ModModel
from account.models import PermissionModel
from account.models import RoleUserModel
from account.models import RoleModModel
from account.models import RolePermissionModel
from utils.onlyone import onlyone


@onlyone.lock(RoleModel.model_sign, 'name:sign', 'sign', 30)
@onlyone.lock(RoleModel.model_sign, 'name', 'name', 30)
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


@onlyone.lock(RoleModel.model_sign, 'obj_id:name:sign', 'sign', 30)
@onlyone.lock(RoleModel.model_sign, 'obj_id:name', 'name', 30)
@onlyone.lock(RoleModel.model_sign, 'obj_id', 'obj_id', 30)
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


@onlyone.lock(RoleModel.model_sign, 'obj_id', 'obj_id', 30)
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


@onlyone.lock(RoleUserModel.model_sign, 'role_id:user_id', 'role_id:user_id', 30)
def create_role_user(role_id, user_id, operator=None):
    '''
    创建角色关联用户
    '''
    query = {
        'user_id': user_id,
        'role_id': role_id,
    }
    if RoleUserModel.objects.filter(**query).exists():
        raise errors.CommonError('用户已关联此角色')
    data = query
    obj = base_ctl.create_obj(RoleUserModel, data, operator)
    data = obj.to_dict()
    return data


@onlyone.lock(RoleUserModel.model_sign, 'role_id:user_id', 'role_id:user_id', 30)
def delete_role_user(role_id, user_id, operator=None):
    '''
    删除角色关联用户
    '''
    query = {
        'user_id': user_id,
        'role_id': role_id,
    }
    obj = RoleUserModel.objects.filter(**query).first()
    if not obj:
        raise errors.CommonError('用户未关联此角色')
    base_ctl.delete_obj(RoleUserModel, obj.id, operator)


def get_role_users(obj_id, page_num=None, page_size=None, operator=None):
    '''
    获取角色用户列表
    '''
    base_query = RoleUserModel.objects.filter(role_id=obj_id)\
            .filter(user__is_deleted=False).select_related('user')
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


@onlyone.lock(RoleModModel.model_sign, 'role_id:mod_id', 'role_id:mod_id', 30)
def create_role_mod(role_id, mod_id, operator=None):
    '''
    创建角色关联模块
    '''
    query = {
        'role_id': role_id,
        'mod_id': mod_id,
    }
    if RoleModModel.objects.filter(**query).exists():
        raise errors.CommonError('角色已关联此模块')
    data = query
    obj = base_ctl.create_obj(RoleModModel, data, operator)
    data = obj.to_dict()
    return data


@onlyone.lock(RoleModModel.model_sign, 'role_id:mod_id', 'role_id:mod_id', 30)
def delete_role_mod(role_id, mod_id, operator=None):
    '''
    删除角色关联模块
    '''
    query = {
        'role_id': role_id,
        'mod_id': mod_id,
    }
    obj = RoleModModel.objects.filter(**query).first()
    if not obj:
        raise errors.CommonError('角色未关联此模块')
    with transaction.atomic():
        base_ctl.delete_obj(RoleModModel, obj.id, operator)


def get_role_mods(obj_id, page_num=None, page_size=None, operator=None):
    '''
    获取角色模块列表
    '''
    base_query = RoleModModel.objects.filter(role_id=obj_id)\
            .filter(user__is_deleted=False).select_related('mod')
    total = base_query.count()
    objs = base_ctl.query_objs_by_page(base_query, page_num, page_size)
    data_list = []
    for obj in objs:
        data = obj.to_dict()
        data['mod'] = obj.mod.to_dict()
        data_list.append(data)
    data = {
        'total': total,
        'data_list': data_list,
    }
    return data


@onlyone.lock(RolePermissionModel.model_sign, 'role_id:permission_id', 'role_id:permission_id', 30)
def create_role_permission(role_id, permission_id, operator=None):
    '''
    创建角色关联权限
    '''
    query = {
        'role_id': role_id,
        'permission_id': permission_id,
    }
    if RolePermissionModel.objects.filter(**query).exists():
        raise errors.CommonError('角色已关联此权限')
    data = query
    with transaction.atomic():
        obj = base_ctl.create_obj(RolePermissionModel, data, operator)
        mod_id = obj.permission.mod_id
        if not RoleModModel.objects.filter(role_id=role_id, mod_id=mod_id).exists():
            data = {
                'role_id': role_id,
                'mod_id': mod_id,
            }
            base_ctl.create_obj(RoleModModel, data)
    data = obj.to_dict()
    return data


@onlyone.lock(RolePermissionModel.model_sign, 'role_id:permission_id', 'role_id:permission_id', 30)
def delete_role_permission(role_id, permission_id, operator=None):
    '''
    删除角色关联权限
    '''
    query = {
        'role_id': role_id,
        'permission_id': permission_id,
    }
    obj = RolePermissionModel.objects.filter(**query).first()
    if not obj:
        raise errors.CommonError('角色未关联此权限')
    base_ctl.delete_obj(RolePermissionModel, obj.id, operator)


def get_role_permissions(obj_id, page_num=None, page_size=None, operator=None):
    '''
    获取角色权限列表
    '''
    base_query = RolePermissionModel.objects.filter(role_id=obj_id)\
            .filter(user__is_deleted=False).select_related('permission')
    total = base_query.count()
    objs = base_ctl.query_objs_by_page(base_query, page_num, page_size)
    data_list = []
    for obj in objs:
        data = obj.to_dict()
        data['permission'] = obj.permission.to_dict()
        data_list.append(data)
    data = {
        'total': total,
        'data_list': data_list,
    }
    return data


def get_roles_by_ids(obj_ids, operator=None):
    '''
    根据角色ID列表获取角色列表
    '''
    objs = RoleModel.objects.filter(id__in=obj_ids).all()
    data_list = [obj.to_dict() for obj in objs]
    return data_list


def get_role_ids_by_user_id(user_id, operator=None):
    '''
    根据user_id获取角色列表
    '''
    role_ids = RoleUserModel.objects.filter(user_id=user_id)\
            .values_list('role_id', flat=True).all()
    return list(set(role_ids))


def get_mods_by_user_id(user_id, operator=None):
    '''
    根据user_id获取模块列表
    '''
    role_ids = get_role_ids_by_user_id(user_id)
    mod_ids = RoleModModel.objects.filter(role_id__in=role_ids).all()
    mods = ModModel.objects.filter(id__in=mod_ids).all()
    return mods


def get_permissions_by_user_id(user_id, operator=None):
    '''
    根据user_id获取权限列表
    '''
    role_ids = get_role_ids_by_user_id(user_id)
    permission_ids = RolePermissionModel.objects.filter(role_id__in=role_ids).all()
    permissions = PermissionModel.objects.filter(id__in=permission_ids).all()
    return permissions
