import ujson as json
from django.db import transaction

from asset.rds.models import RdsModel
from asset.rds.models import RdsAccountModel
from asset.rds.models import RdsDatabaseModel
from asset.rds.models import RdsDatabaseAccountModel
from asset.manager.models import RegionModel
from asset.manager.controllers import aliyun_key as aliyun_key_ctl
from asset.manager.controllers import region as region_ctl
from base import controllers as base_ctl
from utils.time_utils import str2datetime_by_format
from utils.aliyun import AliyunRDS


def format_rds_data(data):
    '''
    格式化RDS返回数据
    '''
    name = data.get('DBInstanceId')
    instance_id = data.get('DBInstanceId')
    desc = data.get('DBInstanceDescription')
    db_net_typ = data.get('DBInstanceNetType')
    net_typ = data.get('InstanceNetworkType')
    db_typ = data.get('DBInstanceType')
    typ = data.get('Engine')
    version = data.get('EngineVersion')
    zone_id = data.get('ZoneId')
    region_id = data.get('RegionId')

    result = {
        'name': name,
        'instance_id': instance_id,
        'desc': desc,
        'db_net_typ': db_net_typ,
        'net_typ': net_typ,
        'db_typ': db_typ,
        'typ': typ,
        'version': version,
        'zone_id': zone_id,
        'region_id': region_id,
    }
    return result


def sync_rdses():
    '''
    同步RDS
    '''
    with transaction.atomic():
        key, secret = aliyun_key_ctl.get_enabled_aliyun_key()
        regions = region_ctl.get_regions(status=RegionModel.ST_ENABLE)['data_list']
        # 记录原来已经创建过的RDS，用于之后删除已经不存在的使用
        old_ids = RdsModel.objects.values_list('id', flat=True).all()
        old_ids = list(set(old_ids))
        # 用来存储仍然可以查到的RDS
        existed_ids = []
        # 记录需要新创建的RDS信息，用于批量创建
        rds_list = []
        # 每次使用都先使用默认的地域初始化，其实可以在类里增加默认值，但是没有增加默认值是为了更明确知道在干什么
        ali_cli = AliyunRDS(key, secret, 'cn-beijing')
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
                data = ali_cli.get_rdses(**query)
                total = data.get('total')
                data_list = data.get('data_list')
                for data in data_list:
                    data = format_rds_data(data)
                    instance_id = data.get('instance_id')
                    attribute = ali_cli.get_rds_attribute(instance_id)
                    if attribute:
                        data['connection'] = attribute.get('ConnectionString')
                    obj = RdsModel.objects.filter(instance_id=instance_id).first()
                    if obj:
                        base_ctl.update_obj(RdsModel, obj.id, data)
                        existed_ids.append(obj.id)
                    else:
                        rds_list.append(data)
                if total <= page_num * page_size:
                    break
                page_num += 1
        base_ctl.create_objs(RdsModel, rds_list)
        deleted_ids = list(set(set(old_ids) - set(existed_ids)))
        base_ctl.delete_objs(RdsModel, deleted_ids)
    sync_rds_accounts()


def sync_rds_accounts():
    '''
    同步RDS账号
    '''
    with transaction.atomic():
        rds_objs = RdsModel.objects.all()
        old_ids = RdsAccountModel.objects.values_list('id', flat=True).all()
        old_ids = list(set(old_ids))
        existed_ids = []
        account_list = []
        key, secret = aliyun_key_ctl.get_enabled_aliyun_key()
        ali_cli = AliyunRDS(key, secret, 'cn-beijing')
        for rds_obj in rds_objs:
            ali_cli.reset_region(rds_obj.region_id)
            page_num = 1
            page_size = 50
            while True:
                query = {
                    'page_num': page_num,
                    'page_size': page_size,
                    'instance_id': rds_obj.instance_id,
                }
                data = ali_cli.get_rds_accounts(**query)
                data_list = data.get('data_list')
                for data in data_list:
                    username = data.get('AccountName')
                    query = {
                        'rds_id': rds_obj.id,
                        'username': username,
                    }
                    obj = RdsAccountModel.objects.filter(**query).first()
                    data = query
                    if not obj:
                        account_list.append(data)
                    else:
                        base_ctl.update_obj(RdsAccountModel, obj.id, data)
                        existed_ids.append(obj.id)
                if page_size > len(data_list):
                    break
                page_num += 1
        base_ctl.create_objs(RdsAccountModel, account_list)
        deleted_ids = list(set(set(old_ids) - set(existed_ids)))
        base_ctl.delete_objs(RdsAccountModel, deleted_ids)
    sync_rds_databases()


def sync_rds_databases():
    '''
    同步RDS Database
    '''
    with transaction.atomic():
        rds_objs = RdsModel.objects.all()
        old_ids = RdsDatabaseModel.objects.values_list('id', flat=True).all()
        old_ids = list(set(old_ids))
        existed_ids = []
        database_list = []
        key, secret = aliyun_key_ctl.get_enabled_aliyun_key()
        ali_cli = AliyunRDS(key, secret, 'cn-beijing')
        for rds_obj in rds_objs:
            ali_cli.reset_region(rds_obj.region_id)
            page_num = 1
            page_size = 50
            while True:
                query = {
                    'page_num': page_num,
                    'page_size': page_size,
                    'instance_id': rds_obj.instance_id,
                }
                data = ali_cli.get_rds_databases(**query)
                data_list = data.get('data_list')
                for data in data_list:
                    instance_id = data.get('DBName')
                    name = data.get('DBName')
                    desc = data.get('DBDescription')
                    # 这里先存一下关联account信息，之后省得再用接口获取
                    accounts = data.get('Accounts').get('AccountPrivilegeInfo')
                    query = {
                        'rds_id': rds_obj.id,
                        'instance_id': instance_id,
                    }
                    obj = RdsDatabaseModel.objects.filter(**query).first()
                    data = query
                    data['name'] = name
                    data['desc'] = desc
                    data['accounts'] = json.dumps(accounts)
                    if not obj:
                        database_list.append(data)
                    else:
                        base_ctl.update_obj(RdsDatabaseModel, obj.id, data)
                        existed_ids.append(obj.id)
                if page_size > len(data_list):
                    break
                page_num += 1
        base_ctl.create_objs(RdsDatabaseModel, database_list)
        deleted_ids = list(set(set(old_ids) - set(existed_ids)))
        base_ctl.delete_objs(RdsDatabaseModel, deleted_ids)
    sync_rds_databases_accounts()


def sync_rds_databases_accounts():
    '''
    同步Database关联Account
    '''
    with transaction.atomic():
        rds_objs = RdsModel.objects.all()
        old_ids = RdsDatabaseAccountModel.objects.values_list('id', flat=True).all()
        old_ids = list(set(old_ids))
        existed_ids = []
        related_list = []
        for rds_obj in rds_objs:
            # 一次取出同一个RDS下所有账号，并形成以username为key、id为value的字典
            accounts = RdsAccountModel.objects.filter(rds_id=rds_obj.id).values_list('username', 'id').all()
            all_account_dict = dict(accounts)

            database_objs = RdsDatabaseModel.objects.filter(rds_id=rds_obj.id).all()
            for database_obj in database_objs:
                accounts = json.loads(database_obj.accounts)
                for account in accounts:
                    username = account.get('Account')
                    privilege = account.get('AccountPrivilege')
                    # 如果username不存在，则说明是同步之前加的就不在此次处理范围
                    if username not in all_account_dict.keys():
                        continue
                    account_id = all_account_dict[username]
                    query = {
                        'database_id': database_obj.id,
                        'account_id': account_id,
                    }
                    obj = RdsDatabaseAccountModel.objects.filter(**query).first()
                    data = query
                    data['privilege'] = privilege
                    if not obj:
                        related_list.append(data)
                    else:
                        base_ctl.update_obj(RdsDatabaseAccountModel, obj.id, data)
                        existed_ids.append(obj.id)
        base_ctl.create_objs(RdsDatabaseAccountModel, related_list)
        deleted_ids = list(set(set(old_ids) - set(existed_ids)))
        base_ctl.delete_objs(RdsDatabaseAccountModel, deleted_ids)
