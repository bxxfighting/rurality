from django.db import transaction
from django.db.models import Q

from base import errors
from base import controllers as base_ctl
from business.service.models import ServiceAssetObjModel
from asset.mongo.models import MongoModel


def create_service_mongo(service_id, environment_id, asset_obj_id, operator=None):
    '''
    创建服务关联Mongo
    '''


def delete_service_mongo(service_id, environment_id, asset_obj_id, operator=None):
    '''
    删除服务关联Mongo
    '''


def get_service_mongos(service_id, environment_id, page_num=None, page_size=None):
    '''
    获取服务关联Mongo列表
    '''
    query = {
        'service_id': service_id,
        'environment_id': environment_id,
        'typ': ServiceAssetObjModel.TYP_MONGO,
    }
    base_query = ServiceAssetObjModel.objects.filter(**query)
    total = base_query.count()
    objs = base_ctl.query_objs_by_page(base_query, page_num, page_size)
    data_list = []
    for obj in objs:
        data = obj.to_dict()
        mongo_obj = base_ctl.get_obj(MongoModel, obj.asset_obj_id)
        data['mongo'] = mongo_obj.to_dict()
        data_list.append(data)
    data = {
        'total': total,
        'data_list': data_list,
    }
    return data
