from django.db import transaction
from django.db.models import Q

from asset.ecs.models import EcsModel
from business.service.models import ServiceAssetObjModel
from base import controllers as base_ctl
from base import errors
from business.service.controllers import asset_obj as asset_obj_ctl
from asset.manager.controllers import aliyun_key as aliyun_key_ctl
from scheduler.controllers import berry as berry_ctl
from utils.onlyone import onlyone


def get_ecses(keyword=None, page_num=None, page_size=None, operator=None):
    '''
    获取ECS列表
    '''
    base_query = EcsModel.objects
    if keyword:
        base_query = base_query.filter(Q(name__icontains=keyword) |
                                       Q(hostname__icontains=keyword) |
                                       Q(inner_ip__icontains=keyword) |
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


def get_ecs_services(obj_id, page_num=None, page_size=None, operator=None):
    '''
    获取ECS关联服务列表
    '''
    query = {
        'asset_obj_id': obj_id,
        'typ': ServiceAssetObjModel.TYP_ECS,
        'page_num': page_num,
        'page_size': page_size,
    }
    return asset_obj_ctl.get_asset_obj_services(**query)


def get_ecs(obj_id, operator=None):
    '''
    获取ECS详情
    '''
    obj = base_ctl.get_obj(EcsModel, obj_id)
    data = obj.to_dict()
    return data


def sync_ecses(operator=None):
    '''
    同步ECS
    '''
    # 先进行是否存在阿里云Key判断
    aliyun_key_ctl.get_enabled_aliyun_key()

    params = {}
    data = {
        'name': '同步ECS',
        'typ': 'sync_ecs',
        'params': params,
    }
    berry_ctl.create_berry(**data)
