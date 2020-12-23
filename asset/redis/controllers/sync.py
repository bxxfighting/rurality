import ujson as json
from django.db import transaction

from asset.redis.models import RedisModel
from asset.redis.models import RedisAccountModel
from asset.manager.models import RegionModel
from asset.manager.controllers import aliyun_key as aliyun_key_ctl
from asset.manager.controllers import region as region_ctl
from base import controllers as base_ctl
from utils.aliyun import AliyunRedis


def format_redis_data(data):
    '''
    格式化Redis返回数据
    '''
    instance_id = data.get('InstanceId')
    name = data.get('InstanceName')
    connection = data.get('ConnectionDomain')
    version = data.get('EngineVersion')
    region_id = data.get('RegionId')
    zone_id = data.get('ZoneId')
    username = data.get('UserName')
    port = data.get('Port')
    inner_ip = data.get('PrivateIp')
    deploy_typ = data.get('ArchitectureType')

    result = {
    	'instance_id': instance_id,
    	'name': name,
    	'connection': connection,
    	'version': version,
    	'region_id': region_id,
    	'zone_id': zone_id,
    	'username': username,
    	'port': port,
    	'inner_ip': inner_ip,
    	'deploy_typ': deploy_typ,
    }
    return result


def sync_redises():
    '''
    同步Redis
    '''
    with transaction.atomic():
        key, secret = aliyun_key_ctl.get_enabled_aliyun_key()
        regions = region_ctl.get_regions(status=RegionModel.ST_ENABLE)['data_list']
        # 记录原来已经创建过的Redis，用于之后删除已经不存在的使用
        old_ids = RedisModel.objects.values_list('id', flat=True).all()
        old_ids = list(set(old_ids))
        # 用来存储仍然可以查到的Redis
        existed_ids = []
        # 记录需要新创建的Redis信息，用于批量创建
        redis_list = []
        # 每次使用都先使用默认的地域初始化，其实可以在类里增加默认值，但是没有增加默认值是为了更明确知道在干什么
        ali_cli = AliyunRedis(key, secret, 'cn-beijing')
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
                data = ali_cli.get_redises(**query)
                total = data.get('total')
                data_list = data.get('data_list')
                for data in data_list:
                    data = format_redis_data(data)
                    instance_id = data.get('instance_id')
                    obj = RedisModel.objects.filter(instance_id=instance_id).first()
                    if obj:
                        base_ctl.update_obj(RedisModel, obj.id, data)
                        existed_ids.append(obj.id)
                    else:
                        redis_list.append(data)
                if total <= page_num * page_size:
                    break
                page_num += 1
        base_ctl.create_objs(RedisModel, redis_list)
        deleted_ids = list(set(set(old_ids) - set(existed_ids)))
        base_ctl.delete_objs(RedisModel, deleted_ids)
    sync_redis_accounts()


def sync_redis_accounts():
    '''
    同步Redis账号
    '''
    with transaction.atomic():
        redis_objs = RedisModel.objects.all()
        old_ids = RedisAccountModel.objects.values_list('id', flat=True).all()
        old_ids = list(set(old_ids))
        existed_ids = []
        account_list = []
        key, secret = aliyun_key_ctl.get_enabled_aliyun_key()
        ali_cli = AliyunRedis(key, secret, 'cn-beijing')
        for redis_obj in redis_objs:
            ali_cli.reset_region(redis_obj.region_id)
            query = {
                'instance_id': redis_obj.instance_id,
            }
            data = ali_cli.get_redis_accounts(**query)
            data_list = data.get('data_list')
            for data in data_list:
                username = data.get('AccountName')
                typ = data.get('AccountType')
                status = data.get('AccountStatus')
                privilege = data.get('DatabasePrivileges').get('DatabasePrivilege')[0].get('AccountPrivilege')
                query = {
                    'redis_id': redis_obj.id,
                    'username': username,
                }
                obj = RedisAccountModel.objects.filter(**query).first()
                data = query
                data['typ'] = typ
                data['status'] = status
                data['privilege'] = privilege
                if not obj:
                    account_list.append(data)
                else:
                    base_ctl.update_obj(RedisAccountModel, obj.id, data)
                    existed_ids.append(obj.id)
        base_ctl.create_objs(RedisAccountModel, account_list)
        deleted_ids = list(set(set(old_ids) - set(existed_ids)))
        base_ctl.delete_objs(RedisAccountModel, deleted_ids)
