from django.db import transaction
from django.db.models import Q

from base import errors
from base import controllers as base_ctl
from business.service.models import ServiceAssetObjModel
from asset.rds.models import RdsDatabaseModel


def create_service_database(service_id, environment_id, asset_obj_id, operator=None):
    '''
    创建服务关联数据库
    '''


def delete_service_database(service_id, environment_id, asset_obj_id, operator=None):
    '''
    删除服务关联数据库
    '''


def get_service_databases(service_id, environment_id, page_num=None, page_size=None):
    '''
    获取服务关联数据库列表
    '''
    query = {
        'service_id': service_id,
        'environment_id': environment_id,
        'typ': ServiceAssetObjModel.TYP_DATABASE,
    }
    base_query = ServiceAssetObjModel.objects.filter(**query)
    total = base_query.count()
    objs = base_ctl.query_objs_by_page(base_query, page_num, page_size)
    data_list = []
    for obj in objs:
        data = obj.to_dict()
        related_obj = base_ctl.get_obj(RdsDatabaseModel, obj.asset_obj_id)
        data['database'] = related_obj.to_dict(is_base=False)
        data_list.append(data)
    data = {
        'total': total,
        'data_list': data_list,
    }
    return data
