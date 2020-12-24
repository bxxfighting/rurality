import ujson as json
from django.db import transaction

from asset.mongo.models import MongoModel
from asset.mongo.models import MongoAccountModel
from asset.manager.models import RegionModel
from asset.manager.controllers import aliyun_key as aliyun_key_ctl
from asset.manager.controllers import region as region_ctl
from base import controllers as base_ctl
from utils.aliyun import AliyunMongo


def format_mongo_data(data):
    '''
    格式化Mongo返回数据
    '''
    instance_id = data.get('DBInstanceId')
    name = data.get('DBInstanceId')
    typ = data.get('Engine')
    version = data.get('EngineVersion')
    region_id = data.get('RegionId')
    zone_id = data.get('ZoneId')
    remark = data.get('DBInstanceDescription')
    db_typ = data.get('DBInstanceType')
    net_typ = data.get('NetworkType')
    replica_count = data.get('ReplicationFactor')

    result = {
        'instance_id': instance_id,
        'name': name,
        'typ': typ,
        'version': version,
        'region_id': region_id,
        'zone_id': zone_id,
        'remark': remark,
        'db_typ': db_typ,
        'net_typ': net_typ,
        'replica_count': replica_count,
    }
    return result


def sync_mongos():
    '''
    同步Mongo
    '''
    with transaction.atomic():
        key, secret = aliyun_key_ctl.get_enabled_aliyun_key()
        regions = region_ctl.get_regions(status=RegionModel.ST_ENABLE)['data_list']
        # 记录原来已经创建过的Mongo，用于之后删除已经不存在的使用
        old_ids = MongoModel.objects.values_list('id', flat=True).all()
        old_ids = list(set(old_ids))
        # 用来存储仍然可以查到的Mongo
        existed_ids = []
        # 记录需要新创建的Mongo信息，用于批量创建
        mongo_list = []
        # 每次使用都先使用默认的地域初始化，其实可以在类里增加默认值，但是没有增加默认值是为了更明确知道在干什么
        ali_cli = AliyunMongo(key, secret, 'cn-beijing')
        for region in regions:
            region_id = region.get('instance_id')
            ali_cli.reset_region(region_id)
            page_num = 1
            page_size = 50
            while True:
                query = {
                    'page_num': page_num,
                    'page_size': page_size,
                }
                data = ali_cli.get_mongos(**query)
                total = data.get('total')
                data_list = data.get('data_list')
                for data in data_list:
                    data = format_mongo_data(data)
                    instance_id = data.get('instance_id')
                    obj = MongoModel.objects.filter(instance_id=instance_id).first()
                    if obj:
                        base_ctl.update_obj(MongoModel, obj.id, data)
                        existed_ids.append(obj.id)
                    else:
                        mongo_list.append(data)
                if total <= page_num * page_size:
                    break
                page_num += 1
        base_ctl.create_objs(MongoModel, mongo_list)
        deleted_ids = list(set(set(old_ids) - set(existed_ids)))
        base_ctl.delete_objs(MongoModel, deleted_ids)
    sync_mongo_accounts()


def sync_mongo_accounts():
    '''
    同步Mongo账号
    '''
    with transaction.atomic():
        mongo_objs = MongoModel.objects.all()
        old_ids = MongoAccountModel.objects.values_list('id', flat=True).all()
        old_ids = list(set(old_ids))
        existed_ids = []
        account_list = []
        key, secret = aliyun_key_ctl.get_enabled_aliyun_key()
        ali_cli = AliyunMongo(key, secret, 'cn-beijing')
        for mongo_obj in mongo_objs:
            ali_cli.reset_region(mongo_obj.region_id)
            query = {
                'instance_id': mongo_obj.instance_id,
            }
            data = ali_cli.get_mongo_accounts(**query)
            data_list = data.get('data_list')
            for data in data_list:
                username = data.get('AccountName')
                typ = data.get('CharacterType')
                status = data.get('AccountStatus')
                remark = data.get('AccountDescription')
                query = {
                    'mongo_id': mongo_obj.id,
                    'username': username,
                }
                obj = MongoAccountModel.objects.filter(**query).first()
                data = query
                data['typ'] = typ
                data['status'] = status
                data['remark'] = remark
                if not obj:
                    account_list.append(data)
                else:
                    base_ctl.update_obj(MongoAccountModel, obj.id, data)
                    existed_ids.append(obj.id)
        base_ctl.create_objs(MongoAccountModel, account_list)
        deleted_ids = list(set(set(old_ids) - set(existed_ids)))
        base_ctl.delete_objs(MongoAccountModel, deleted_ids)
