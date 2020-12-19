from django.db import transaction
from django.db.models import Q

from asset.ecs.models import EcsModel
from asset.slb.models import SlbServerGroupModel
from asset.slb.models import SlbServerGroupEcsModel
from business.service.models import ServiceAssetObjModel
from business.service.controllers import asset_obj as asset_obj_ctl
from base import controllers as base_ctl
from base import errors


def get_server_groups(slb_id=None, slb_instance_id=None, keyword=None, page_num=None, page_size=None, operator=None):
    '''
    获取SLB服务器组列表
    '''
    if not slb_id and not slb_instance_id:
        raise errors.CommonError('缺少SLB ID或SLB实例ID')
    base_query = SlbServerGroupModel.objects
    if slb_id:
        base_query = base_query.filter(slb_id=slb_id)
    else:
        base_query = base_query.filter(slb__instance_id=slb_instance_id)

    if keyword:
        base_query = base_query.filter(Q(name__icontains=keyword) |
                                       Q(instance_id__icontains=keyword))
    total = base_query.count()
    objs = base_ctl.query_objs_by_page(base_query, page_num, page_size)
    data_list = []
    for obj in objs:
        data = obj.to_dict()
        data['slb'] = obj.slb.to_dict()
        data_list.append(data)
    data = {
        'total': total,
        'data_list': data_list,
    }
    return data


def get_server_group(obj_id, operator=None):
    '''
    获取SLB服务器组详情
    '''
    obj = base_ctl.get_obj(SlbServerGroupModel, obj_id)
    data = obj.to_dict()
    data['slb'] = obj.slb.to_dict()
    return data


def get_server_group_ecses(obj_id, keyword=None, page_num=None, page_size=None, operator=None):
    '''
    获取SLb服务器组下ECS列表
    '''
    base_query = SlbServerGroupEcsModel.objects.filter(server_group_id=obj_id)
    if keyword:
        ecs_ids = EcsModel.objects.filter(Q(name__icontains=keyword) |
                                Q(hostname__icontains=keyword) |
                                Q(inner_ip__icontains=keyword) |
                                Q(instance_id__icontains=keyword))\
                                        .values_list('id', flat=True).all()
        base_query = base_query.filter(ecs_id__in=ecs_ids)
    total = base_query.count()
    objs = base_ctl.query_objs_by_page(base_query, page_num, page_size)
    data_list = []
    for obj in objs:
        data = obj.to_dict()
        data['ecs'] = obj.ecs.to_dict()
        data_list.append(data)
    data = {
        'total': total,
        'data_list': data_list,
    }
    return data


def get_server_group_services(obj_id, page_num=None, page_size=None, operator=None):
    '''
    获取SLB服务器组关联服务列表
    '''
    query = {
        'asset_obj_id': obj_id,
        'typ': ServiceAssetObjModel.TYP_SLB_SERVER_GROUP,
        'page_num': page_num,
        'page_size': page_size,
    }
    return asset_obj_ctl.get_asset_obj_services(**query)
