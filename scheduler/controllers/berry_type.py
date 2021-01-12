from django.db import transaction
from django.db.models import Q

from scheduler.models import BerryTypeModel
from base import controllers as base_ctl
from base import errors
from utils.onlyone import onlyone


@onlyone.lock(BerryTypeModel.model_sign, 'name:sign', 'sign', 30)
@onlyone.lock(BerryTypeModel.model_sign, 'name:sign', 'name', 30)
def create_berry_type(name, sign, parent_id, operator=None):
    '''
    创建任务类型
    '''
    query = {
        'name': name,
    }
    if BerryTypeModel.objects.filter(**query).exists():
        raise errors.CommonError('任务类型名称已经存在')
    query = {
        'sign': sign,
    }
    if BerryTypeModel.objects.filter(**query).exists():
        raise errors.CommonError('任务类型标识已经存在')
    data = {
        'name': name,
        'sign': sign,
        'parent_id': parent_id,
    }
    obj = base_ctl.create_obj(BerryTypeModel, data, operator)
    data = obj.to_dict()
    return data


@onlyone.lock(BerryTypeModel.model_sign, 'obj_id:name:sign', 'sign', 30)
@onlyone.lock(BerryTypeModel.model_sign, 'obj_id:name:sign', 'name', 30)
@onlyone.lock(BerryTypeModel.model_sign, 'obj_id', 'obj_id', 30)
def update_berry_type(obj_id, name, sign, parent_id, operator=None):
    '''
    编辑任务类型
    '''
    query = {
        'name': name,
    }
    if BerryTypeModel.objects.filter(**query).exclude(id=obj_id).exists():
        raise errors.CommonError('任务类型名称已经存在')
    query = {
        'sign': sign,
    }
    if BerryTypeModel.objects.filter(**query).exclude(id=obj_id).exists():
        raise errors.CommonError('任务类型标识已经存在')
    data = {
        'name': name,
        'sign': sign,
        'parent_id': parent_id,
    }
    obj = base_ctl.update_obj(BerryTypeModel, obj_id, data, operator)
    data = obj.to_dict()
    return data


@onlyone.lock(BerryTypeModel.model_sign, 'obj_id', 'obj_id', 30)
def delete_berry_type(obj_id, operator=None):
    '''
    删除任务类型
    '''
    query = {
        'parent_id': obj_id
    }
    if BerryTypeModel.objects.filter(**query).exists():
        raise errors.CommonError('存在子类型，不允许删除')
    base_ctl.delete_obj(BerryTypeModel, obj_id, operator)


def get_berry_types(parent_id=None, page_num=None, page_size=None, operator=None):
    '''
    获取任务类型列表
    '''
    base_query = BerryTypeModel.objects.filter(parent_id=parent_id)
    total = base_query.count()
    objs = base_ctl.query_objs_by_page(base_query, page_num, page_size)
    data_list = [obj.to_dict() for obj in objs]
    data = {
        'total': total,
        'data_list': data_list,
    }
    return data


def get_berry_type(obj_id, operator=None):
    '''
    获取任务类型信息
    '''
    obj = base_ctl.get_obj(BerryTypeModel, obj_id)
    data = obj.to_dict()
    return data
