from django.db import transaction
from django.db.models import Q

from base import errors
from base import controllers as base_ctl
from business.project.models import ProjectModel
from business.project.models import ProjectUserModel
from business.service import controllers as service_ctl
from utils.onlyone import onlyone


@onlyone.lock(ProjectModel.model_sign, 'name', 'name', 30)
def create_project(name, remark=None, operator=None):
    '''
    创建项目
    '''
    if ProjectModel.objects.filter(name=name).exists():
        raise errors.CommonError('项目名称已存在')
    data = {
        'name': name,
        'remark': remark,
    }
    obj = base_ctl.create_obj(ProjectModel, data, operator)
    data = obj.to_dict()
    return data


@onlyone.lock(ProjectModel.model_sign, 'obj_id:name', 'name', 30)
@onlyone.lock(ProjectModel.model_sign, 'obj_id', 'obj_id', 30)
def update_project(obj_id, name, remark=None, operator=None):
    '''
    编辑项目
    '''
    if ProjectModel.objects.filter(name=name).exclude(id=obj_id).exists():
        raise errors.CommonError('项目名称已存在')
    data = {
        'name': name,
        'remark': remark,
    }
    obj = base_ctl.update_obj(ProjectModel, obj_id, data, operator)
    data = obj.to_dict()
    return data


@onlyone.lock(ProjectModel.model_sign, 'obj_id', 'obj_id', 30)
def delete_project(obj_id, operator=None):
    '''
    删除项目
    '''
    base_ctl.delete_obj(ProjectModel, obj_id, operator)


def get_projects(keyword=None, page_num=None, page_size=None, operator=None):
    '''
    获取项目列表
    '''
    base_query = ProjectModel.objects
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


def get_project(obj_id, operator=None):
    '''
    获取项目信息
    '''
    obj = base_ctl.get_obj(ProjectModel, obj_id)
    data = obj.to_dict()
    return data


@onlyone.lock(ProjectUserModel.model_sign, 'obj_id:user_id', 'obj_id:user_id', 30)
def create_project_user(obj_id, user_id, typ, operator=None):
    '''
    创建项目关联用户
    '''
    query = {
        'project_id': obj_id,
        'user_id': user_id,
    }
    if ProjectUserModel.objects.filter(**query).exists():
        raise errors.CommonError('用户已在此项目中')
    if not ProjectUserModel.check_choices('typ', typ):
        raise errors.CommonError('类型值不正确')
    data = {
        'project_id': obj_id,
        'user_id': user_id,
        'typ': typ,
    }
    obj = base_ctl.create_obj(ProjectUserModel, data, operator)
    data = obj.to_dict()
    return data


@onlyone.lock(ProjectUserModel.model_sign, 'obj_id:user_id', 'obj_id:user_id', 30)
def update_project_user(obj_id, user_id, typ, operator=None):
    '''
    编辑项目关联用户
    '''
    query = {
        'project_id': obj_id,
        'user_id': user_id,
    }
    obj = ProjectUserModel.objects.filter(**query).first()
    if not obj:
        raise errors.CommonError('用户未在此项目')
    if not ProjectUserModel.check_choices('typ', typ):
        raise errors.CommonError('类型值不正确')
    data = {
        'typ': typ,
    }
    obj = base_ctl.update_obj(ProjectUserModel, obj.id, data, operator)
    data = obj.to_dict()
    return data


@onlyone.lock(ProjectUserModel.model_sign, 'obj_id:user_id', 'obj_id:user_id', 30)
def delete_project_user(obj_id, user_id, operator=None):
    '''
    删除项目关联用户
    '''
    query = {
        'project_id': obj_id,
        'user_id': user_id,
    }
    obj = ProjectUserModel.objects.filter(**query).first()
    if not obj:
        raise errors.CommonError('用户未在此项目中')
    base_ctl.delete_obj(ProjectUserModel, obj.id, operator)


def get_project_users(obj_id, typ=None, page_num=None, page_size=None, operator=None):
    '''
    获取项目用户列表
    '''
    base_query = ProjectUserModel.objects.filter(project_id=obj_id)\
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


def get_project_services(obj_id, keyword=None, page_num=None, page_size=None, operator=None):
    '''
    获取项目服务列表
    '''
    query = {
        'keyword': keyword,
        'project_id': obj_id,
        'page_num': page_num,
        'page_size': page_size,
    }
    data = service_ctl.get_services(**query)
    return data
