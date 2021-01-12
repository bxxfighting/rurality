from django.db import transaction
from django.db.models import Q

from asset.rocket.models import RocketModel
from business.service.models import ServiceAssetObjModel
from business.service.controllers import asset_obj as asset_obj_ctl
from asset.manager.controllers import aliyun_key as aliyun_key_ctl
from scheduler.controllers import berry as berry_ctl
from base import controllers as base_ctl


def get_rockets(keyword=None, page_num=None, page_size=None, operator=None):
    '''
    获取Rocket列表
    '''
    base_query = RocketModel.objects
    if keyword:
        base_query = base_query.filter(Q(name__icontains=keyword) |
                                       Q(instance_id__icontains=keyword))
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


def get_rocket(obj_id, operator=None):
    '''
    获取Rocket详情
    '''
    obj = base_ctl.get_obj(RocketModel, obj_id)
    data = obj.to_dict()
    return data


def sync_rockets(operator=None):
    '''
    同步Rocket
    '''
    aliyun_key_ctl.get_enabled_aliyun_key()
    params = {}
    data = {
        'name': '同步Rocket',
        'typ': 'sync_rocket',
        'params': params,
    }
    berry_ctl.create_berry(**data)
