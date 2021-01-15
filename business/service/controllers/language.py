from django.db import transaction
from django.db.models import Q

from base import errors
from base import controllers as base_ctl
from business.service.models import LanguageModel
from utils.onlyone import onlyone


@onlyone.lock(LanguageModel.model_sign, 'name:sign', 'sign', 30)
@onlyone.lock(LanguageModel.model_sign, 'name', 'name', 30)
def create_language(name, sign, operator=None):
    '''
    创建编程语言
    '''
    if LanguageModel.objects.filter(name=name).exists():
        raise errors.CommonError('编程语言名称已存在')
    if LanguageModel.objects.filter(sign=sign).exists():
        raise errors.CommonError('编程语言标识已存在')
    data = {
        'name': name,
        'sign': sign,
    }
    obj = base_ctl.create_obj(LanguageModel, data, operator)
    data = obj.to_dict()
    return data


@onlyone.lock(LanguageModel.model_sign, 'obj_id:name:sign', 'sign', 30)
@onlyone.lock(LanguageModel.model_sign, 'obj_id:name', 'name', 30)
@onlyone.lock(LanguageModel.model_sign, 'obj_id', 'obj_id', 30)
def update_language(obj_id, name, sign, operator=None):
    '''
    编辑编程语言
    '''
    if LanguageModel.objects.filter(name=name).exclude(id=obj_id).exists():
        raise errors.CommonError('编程语言名称已存在')
    if LanguageModel.objects.filter(sign=sign).exclude(id=obj_id).exists():
        raise errors.CommonError('编程语言标识已存在')
    data = {
        'name': name,
        'sign': sign,
    }
    obj = base_ctl.update_obj(LanguageModel, obj_id, data, operator)
    data = obj.to_dict()
    return data


@onlyone.lock(LanguageModel.model_sign, 'obj_id', 'obj_id', 30)
def delete_language(obj_id, operator=None):
    '''
    删除编程语言
    '''
    # TODO: 增加不可删除判断
    base_ctl.delete_obj(LanguageModel, obj_id, operator)


def get_languages(page_num=None, page_size=None, operator=None):
    '''
    获取编程语言列表
    '''
    base_query = LanguageModel.objects
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


def get_language(obj_id, operator=None):
    '''
    获取编程语言信息
    '''
    obj = base_ctl.get_obj(LanguageModel, obj_id)
    data = obj.to_dict()
    return data
