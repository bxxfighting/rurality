from django.db import transaction
from django.db.models import Q

from base import errors
from base import controllers as base_ctl
from business.service.models import ServiceAssetObjModel
from asset.slb.models import SlbServerGroupModel


def create_service_server_group(service_id, environment_id, asset_obj_id, operator=None):
    '''
    创建服务关联SLB服务器组
    '''


def delete_service_server_group(service_id, environment_id, asset_obj_id, operator=None):
    '''
    删除服务关联SLB服务器组
    '''


def get_service_server_groups(service_id, environment_id, page_num=None, page_size=None):
    '''
    获取服务关联SLB服务器组列表
    '''
    query = {
        'service_id': service_id,
        'environment_id': environment_id,
        'typ': ServiceAssetObjModel.TYP_SLB_SERVER_GROUP,
    }
    base_query = ServiceAssetObjModel.objects.filter(**query)
    total = base_query.count()
    objs = base_ctl.query_objs_by_page(base_query, page_num, page_size)
    data_list = []
    for obj in objs:
        data = obj.to_dict()
        server_group_obj = base_ctl.get_obj(SlbServerGroupModel, obj.asset_obj_id)
        data['server_group'] = server_group_obj.to_dict(is_base=False)
        data_list.append(data)
    data = {
        'total': total,
        'data_list': data_list,
    }
    return data
