from django.db import transaction
from django.db.models import Q

from base import errors
from base import controllers as base_ctl
from business.service.models import ServiceAssetModel
from business.service.models import ServiceAssetObjModel
from asset.ecs.models import EcsModel
from asset.slb.models import SlbServerGroupModel
from asset.rds.models import RdsDatabaseModel
from asset.redis.models import RedisModel
from asset.mongo.models import MongoModel
from asset.domain.models import DomainRecordModel
from asset.rocket.models import RocketTopicModel
from business.service.controllers import ecs as ecs_ctl
from business.service.controllers import server_group as server_group_ctl
from business.service.controllers import database as database_ctl
from business.service.controllers import redis as redis_ctl
from business.service.controllers import mongo as mongo_ctl
from business.service.controllers import domain as domain_ctl
from business.service.controllers import rocket_topic as rocket_topic_ctl
from utils.onlyone import onlyone


def is_existed_asset_obj(typ, asset_obj_id):
    '''
    判断资产实例是否存在
    '''
    if typ == ServiceAssetObjModel.TYP_ECS:
        return EcsModel.objects.filter(id=asset_obj_id).exists()
    elif typ == ServiceAssetObjModel.TYP_SLB_SERVER_GROUP:
        return SlbServerGroupModel.objects.filter(id=asset_obj_id).exists()
    elif typ == ServiceAssetObjModel.TYP_DATABASE:
        return RdsDatabaseModel.objects.filter(id=asset_obj_id).exists()
    elif typ == ServiceAssetObjModel.TYP_REDIS:
        return RedisModel.objects.filter(id=asset_obj_id).exists()
    elif typ == ServiceAssetObjModel.TYP_MONGO:
        return MongoModel.objects.filter(id=asset_obj_id).exists()
    elif typ == ServiceAssetObjModel.TYP_DOMAIN:
        return DomainRecordModel.objects.filter(id=asset_obj_id).exists()
    elif typ == ServiceAssetObjModel.TYP_ROCKET_TOPIC:
        return RocketTopicModel.objects.filter(id=asset_obj_id).exists()
    return False


@onlyone.lock(ServiceAssetObjModel.model_sign, 'obj_id:environment_id:typ:asset_obj_id',\
        'obj_id:environment_id:typ:asset_obj_id', 30)
def create_service_asset_obj(obj_id, environment_id, typ, asset_obj_id, operator=None):
    '''
    创建服务关联资产实例
    '''
    # 零：判断typ值
    if not ServiceAssetObjModel.check_choices('typ', typ):
        raise errors.CommonError('资产实例类型值不正确')
    # 一：判断服务是否关联对应资产模块
    query = {
        'service_id': obj_id,
        'asset__sign': typ,
    }
    if not ServiceAssetModel.objects.filter(**query).exists():
        raise errors.CommonError('服务需要先关联此资产模块')
    # 二：判断资产实例是否存在
    if not is_existed_asset_obj(typ, asset_obj_id):
        raise errors.CommonError('资产实例不存在')
    # 三：判断是否已经关联此资产实例
    query = {
        'service_id': obj_id,
        'environment_id': environment_id,
        'typ': typ,
        'asset_obj_id': asset_obj_id,
        'status': ServiceAssetObjModel.ST_PENDING_ADD,
    }
    if ServiceAssetObjModel.objects.filter(**query).exists():
        raise errors.CommonError('服务已关联此资产实例')
    # 四：建立关联关系
    data = query
    obj = base_ctl.create_obj(ServiceAssetObjModel, data, operator)
    #TODO 五：调用异步任务完成添加的具体操作
    data = obj.to_dict()
    return data


@onlyone.lock(ServiceAssetObjModel.model_sign, 'obj_id:environment_id:typ:asset_obj_id',\
        'obj_id:environment_id:typ:asset_obj_id', 30)
def delete_service_asset_obj(obj_id, environment_id, typ, asset_obj_id, operator=None):
    '''
    删除服务关联资产实例
    '''
    # 零：判断typ值
    if not ServiceAssetObjModel.check_choices('typ', typ):
        raise errors.CommonError('资产实例类型值不正确')
    # 一：判断服务是否关联对应资产模块
    query = {
        'service_id': obj_id,
        'asset__sign': typ,
    }
    if not ServiceAssetModel.objects.filter(**query).exists():
        raise errors.CommonError('服务需要先关联此资产模块')
    # 二：判断资产实例是否存在
    if not is_existed_asset_obj(typ, asset_obj_id):
        raise errors.CommonError('资产实例不存在')
    # 三：判断是否已经关联此资产实例
    query = {
        'service_id': obj_id,
        'environment_id': environment_id,
        'typ': typ,
        'asset_obj_id': asset_obj_id,
    }
    obj = ServiceAssetObjModel.objects.filter(**query).first()
    if not obj:
        raise errors.CommonError('服务未关联此资产实例')
    data = {
        'status': ServiceAssetObjModel.ST_PENDING_REMOVE,
    }
    base_ctl.update_obj(ServiceAssetObjModel, obj.id, data, operator)
    #TODO 五：调用异步任务完成删除的具体操作，完成后再删除关联关系


def get_service_asset_objs(obj_id, environment_id, typ, page_num=None, page_size=None, operator=None):
    '''
    获取服务关联资产实例列表
    '''
    # 零：判断typ值
    if not ServiceAssetObjModel.check_choices('typ', typ):
        raise errors.CommonError('资产实例类型值不正确')

    # 一：判断服务是否关联对应资产模块
    query = {
        'service_id': obj_id,
        'asset__sign': typ,
    }
    if not ServiceAssetModel.objects.filter(**query).exists():
        raise errors.CommonError('服务需要先关联此资产模块')

    data = {
        'total': 0,
        'data_list': [],
    }
    query = {
        'service_id': obj_id,
        'environment_id': environment_id,
        'page_num': page_num,
        'page_size': page_size,
    }
    if typ == ServiceAssetObjModel.TYP_ECS:
        data = ecs_ctl.get_service_ecses(**query)
    elif typ == ServiceAssetObjModel.TYP_SLB_SERVER_GROUP:
        data = server_group_ctl.get_service_server_groups(**query)
    elif typ == ServiceAssetObjModel.TYP_DATABASE:
        data = database_ctl.get_service_databases(**query)
    elif typ == ServiceAssetObjModel.TYP_REDIS:
        data = redis_ctl.get_service_redises(**query)
    elif typ == ServiceAssetObjModel.TYP_MONGO:
        data = mongo_ctl.get_service_mongos(**query)
    elif typ == ServiceAssetObjModel.TYP_DOMAIN:
        data = domain_ctl.get_service_domains(**query)
    elif typ == ServiceAssetObjModel.TYP_ROCKET_TOPIC:
        data = rocket_topic_ctl.get_service_rocket_topics(**query)

    return data


def get_asset_obj_services(asset_obj_id, typ, page_num=None, page_size=None, operator=None):
    '''
    获取资产实例服务列表
    '''
    query = {
        'asset_obj_id': asset_obj_id,
        'typ': typ,
    }

    base_query = ServiceAssetObjModel.objects.filter(**query)
    total = base_query.count()
    objs = base_ctl.query_objs_by_page(base_query, page_num, page_size)
    data_list = []
    for obj in objs:
        data = obj.to_dict()
        data['service'] = obj.service.to_dict()
        data['environment'] = obj.environment.to_dict()
        data_list.append(data)
    data = {
        'total': total,
        'data_list': data_list,
    }
    return data
