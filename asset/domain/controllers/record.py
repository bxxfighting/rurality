from django.db import transaction
from django.db.models import Q

from asset.domain.models import DomainRecordModel
from asset.domain.models import DomainRecordAssetModel
from asset.ecs.models import EcsModel
from asset.slb.models import SlbModel
from business.service.models import ServiceAssetObjModel
from business.service.controllers import asset_obj as asset_obj_ctl
from base import controllers as base_ctl


def get_domain_records(domain_id=None, keyword=None, page_num=None, page_size=None, operator=None):
    '''
    获取解析记录列表
    '''
    base_query = DomainRecordModel.objects
    if domain_id:
        base_query = base_query.filter(domain_id=domain_id)
    if keyword:
        base_query = base_query.filter(Q(fullname__icontains=keyword) |
                                       Q(value__icontains=keyword) |
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


def get_domain_record_asset(record_id):
    asset = DomainRecordAssetModel.objects.filter(record_id=record_id).first()
    if not asset:
        return
    data = None

    if asset.typ == DomainRecordAssetModel.TYP_ECS:
        obj = base_ctl.get_obj(EcsModel, asset.asset_obj_id)
        data = {
            'id': obj.id,
            'name': obj.name,
            'typ': DomainRecordAssetModel.TYP_ECS,
        }
    elif asset.typ == DomainRecordAssetModel.TYP_SLB:
        obj = base_ctl.get_obj(SlbModel, asset.asset_obj_id)
        data = {
            'id': obj.id,
            'name': obj.name,
            'typ': DomainRecordAssetModel.TYP_SLB,
        }
    return data


def get_domain_record(obj_id, operator=None):
    '''
    获取解析记录详情
    '''
    obj = base_ctl.get_obj(DomainRecordModel, obj_id)
    data = obj.to_dict()
    data['asset'] = get_domain_record_asset(obj.id)
    data['domain'] = obj.domain.to_dict()
    return data


def get_domain_record_services(obj_id, page_num=None, page_size=None, operator=None):
    '''
    获取解析记录关联服务列表
    '''
    query = {
        'asset_obj_id': obj_id,
        'typ': ServiceAssetObjModel.TYP_DOMAIN,
        'page_num': page_num,
        'page_size': page_size,
    }
    return asset_obj_ctl.get_asset_obj_services(**query)
