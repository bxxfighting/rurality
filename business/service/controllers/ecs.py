from django.db import transaction
from django.db.models import Q

from base import errors
from base import controllers as base_ctl
from business.service.models import ServiceAssetObjModel
from asset.ecs.models import EcsModel


def create_service_ecs(service_id, environment_id, asset_obj_id, operator=None):
    '''
    创建服务关联ECS
    '''


def delete_service_ecs(service_id, environment_id, asset_obj_id, operator=None):
    '''
    删除服务关联ECS
    '''


def get_service_ecses(service_id, environment_id, page_num=None, page_size=None):
    '''
    获取服务关联ECS列表
    '''
    query = {
        'service_id': service_id,
        'environment_id': environment_id,
        'typ': ServiceAssetObjModel.TYP_ECS,
    }
    base_query = ServiceAssetObjModel.objects.filter(**query)
    total = base_query.count()
    objs = base_ctl.query_objs_by_page(base_query, page_num, page_size)
    data_list = []
    for obj in objs:
        data = obj.to_dict()
        ecs_obj = base_ctl.get_obj(EcsModel, obj.asset_obj_id)
        data['ecs'] = ecs_obj.to_dict()
        data_list.append(data)
    data = {
        'total': total,
        'data_list': data_list,
    }
    return data
