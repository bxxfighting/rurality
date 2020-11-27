from django.db import transaction
from django.db.models import Q

from base import errors
from base import controllers as base_ctl
from business.service.models import EnvironmentModel
from utils.onlyone import onlyone


@onlyone.lock(EnvironmentModel.model_sign, 'name:sign', 'sign', 30)
@onlyone.lock(EnvironmentModel.model_sign, 'name', 'name', 30)
def create_environment(name, sign, rank=0, remark='', operator=None):
    '''
    创建环境
    '''
    if EnvironmentModel.objects.filter(name=name).exists():
        raise errors.CommonError('环境名称已存在')
    if EnvironmentModel.objects.filter(sign=sign).exists():
        raise errors.CommonError('环境标识已存在')
    data = {
        'name': name,
        'sign': sign,
        'rank': rank,
        'remark': remark,
    }
    obj = base_ctl.create_obj(EnvironmentModel, data, operator)
    data = obj.to_dict()
    return data


@onlyone.lock(EnvironmentModel.model_sign, 'obj_id:name:sign', 'sign', 30)
@onlyone.lock(EnvironmentModel.model_sign, 'obj_id:name', 'name', 30)
@onlyone.lock(EnvironmentModel.model_sign, 'obj_id', 'obj_id', 30)
def update_environment(obj_id, name, sign, rank=0, remark=None, operator=None):
    '''
    编辑环境
    '''
    if EnvironmentModel.objects.filter(name=name).exclude(id=obj_id).exists():
        raise errors.CommonError('环境名称已存在')
    if EnvironmentModel.objects.filter(sign=sign).exclude(id=obj_id).exists():
        raise errors.CommonError('环境标识已存在')
    data = {
        'name': name,
        'sign': sign,
        'rank': rank,
        'remark': remark,
    }
    obj = base_ctl.update_obj(EnvironmentModel, obj_id, data, operator)
    data = obj.to_dict()
    return data


@onlyone.lock(EnvironmentModel.model_sign, 'obj_id', 'obj_id', 30)
def delete_environment(obj_id, operator=None):
    '''
    删除环境
    '''
    # TODO: 增加不允许删除的限制
    base_ctl.delete_obj(EnvironmentModel, obj_id, operator)


def get_environments(page_num=None, page_size=None, operator=None):
    '''
    获取环境列表
    '''
    base_query = EnvironmentModel.objects
    # TODO: 环境列表最后要加权限控制，并不是每个人都可以看到所有环境
    # 最简单的控制就是区分线上环境和其它测试类环境
    total = base_query.count()
    objs = base_ctl.query_objs_by_page(base_query, page_num, page_size)
    data_list = []
    for obj in objs:
        data = obj.to_dict()
        data_list.append(data)
    data = {
        'total': total,
        'data_list': data_list,
    }
    return data


def get_environment(obj_id, operator=None):
    '''
    获取环境信息
    '''
    obj = base_ctl.get_obj(EnvironmentModel, obj_id)
    data = obj.to_dict()
    return data
