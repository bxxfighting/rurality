from django.db import transaction
from django.db.models import Q

from base import errors
from base import controllers as base_ctl
from business.service.models import FrameModel
from utils.onlyone import onlyone


@onlyone.lock(FrameModel.model_sign, 'name:sign', 'sign', 30)
@onlyone.lock(FrameModel.model_sign, 'name', 'name', 30)
def create_frame(name, sign, language_id, operator=None):
    '''
    创建框架
    '''
    if FrameModel.objects.filter(name=name).exists():
        raise errors.CommonError('框架名称已存在')
    if FrameModel.objects.filter(sign=sign).exists():
        raise errors.CommonError('框架标识已存在')
    data = {
        'name': name,
        'sign': sign,
        'language_id': language_id,
    }
    obj = base_ctl.create_obj(FrameModel, data, operator)
    data = obj.to_dict()
    return data


@onlyone.lock(FrameModel.model_sign, 'obj_id:name:sign', 'sign', 30)
@onlyone.lock(FrameModel.model_sign, 'obj_id:name', 'name', 30)
@onlyone.lock(FrameModel.model_sign, 'obj_id', 'obj_id', 30)
def update_frame(obj_id, name, sign, language_id, operator=None):
    '''
    编辑框架
    '''
    if FrameModel.objects.filter(name=name).exclude(id=obj_id).exists():
        raise errors.CommonError('框架名称已存在')
    if FrameModel.objects.filter(sign=sign).exclude(id=obj_id).exists():
        raise errors.CommonError('框架标识已存在')
    data = {
        'name': name,
        'sign': sign,
        'language_id': language_id,
    }
    obj = base_ctl.update_obj(FrameModel, obj_id, data, operator)
    data = obj.to_dict()
    return data


@onlyone.lock(FrameModel.model_sign, 'obj_id', 'obj_id', 30)
def delete_frame(obj_id, operator=None):
    '''
    删除框架
    '''
    # TODO: 增加不可删除判断
    base_ctl.delete_obj(FrameModel, obj_id, operator)


def get_frames(language_id=None, page_num=None, page_size=None, operator=None):
    '''
    获取框架列表
    '''
    base_query = FrameModel.objects
    if language_id:
        base_query = base_query.filter(language_id=language_id)
    total = base_query.count()
    objs = base_ctl.query_objs_by_page(base_query, page_num, page_size)
    data_list = []
    for obj in objs:
        data = obj.to_dict()
        if not language_id:
            data['language'] = obj.language.to_dict()
        data_list.append(data)
    data = {
        'total': total,
        'data_list': data_list,
    }
    return data


def get_frame(obj_id, operator=None):
    '''
    获取框架信息
    '''
    obj = base_ctl.get_obj(FrameModel, obj_id)
    data = obj.to_dict()
    data['language'] = obj.language.to_dict()
    return data
