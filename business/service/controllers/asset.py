from django.db import transaction
from django.db.models import Q

from base import errors
from base import controllers as base_ctl
from business.service.models import ServiceAssetModel
from asset.manager.models import AssetModel
from utils.onlyone import onlyone


@onlyone.lock(ServiceAssetModel.model_sign, 'obj_id:asset_id', 'obj_id:asset_id', 30)
def create_service_asset(obj_id, asset_id, operator=None):
    '''
    创建服务关联资产模块
    '''
    query = {
        'service_id': obj_id,
        'asset_id': asset_id,
    }
    if ServiceAssetModel.objects.filter(**query).exists():
        raise errors.CommonError('服务已关联此资产模块')
    data = query
    obj = base_ctl.create_obj(ServiceAssetModel, data, operator)
    data = obj.to_dict()
    return data


@onlyone.lock(ServiceAssetModel.model_sign, 'obj_id:asset_id', 'obj_id:asset_id', 30)
def delete_service_asset(obj_id, asset_id, operator=None):
    '''
    删除服务关联资产模块
    '''
    query = {
        'service_id': obj_id,
        'asset_id': asset_id,
    }
    obj = ServiceAssetModel.objects.filter(**query).first()
    if not obj:
        raise errors.CommonError('服务未关联此资产模块')
    base_ctl.delete_obj(ServiceAssetModel, obj.id, operator)


def get_service_assets(obj_id, page_num=None, page_size=None, operator=None):
    '''
    获取服务关联资产模块列表
    '''
    batch_ids = ServiceAssetModel.objects.filter(service_id=obj_id)\
            .values_list('asset_id', flat=True).all()

    base_query = AssetModel.objects.filter(id__in=batch_ids)
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
