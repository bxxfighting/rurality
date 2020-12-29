import ujson as json
from django.db import transaction
from django.db.models import Q

from asset.domain.models import DomainModel
from asset.domain.models import DomainRecordModel
from asset.domain.models import DomainRecordAssetModel
from asset.ecs.models import EcsModel
from asset.slb.models import SlbModel
from asset.manager.models import RegionModel
from asset.manager.controllers import aliyun_key as aliyun_key_ctl
from asset.manager.controllers import region as region_ctl
from base import controllers as base_ctl
from utils.aliyun import AliyunDNS


def format_domain_data(data):
    '''
    格式化Domain返回数据
    '''
    name = data.get('DomainName')
    instance_id = data.get('DomainId')
    record_count = data.get('RecordCount')

    result = {
        'instance_id': instance_id,
        'name': name,
        'record_count': record_count,
    }
    return result


def sync_domains():
    '''
    同步Domain
    '''
    with transaction.atomic():
        key, secret = aliyun_key_ctl.get_enabled_aliyun_key()
        # 记录原来已经创建过的Domain，用于之后删除已经不存在的使用
        old_ids = DomainModel.objects.values_list('id', flat=True).all()
        old_ids = list(set(old_ids))
        # 用来存储仍然可以查到的Domain
        existed_ids = []
        # 记录需要新创建的Domain信息，用于批量创建
        domain_list = []
        # 每次使用都先使用默认的地域初始化，其实可以在类里增加默认值，但是没有增加默认值是为了更明确知道在干什么
        ali_cli = AliyunDNS(key, secret, 'cn-beijing')
        page_num = 1
        page_size = 50
        while True:
            query = {
                'page_num': page_num,
                'page_size': page_size,
            }
            data = ali_cli.get_domains(**query)
            total = data.get('total')
            data_list = data.get('data_list')
            for data in data_list:
                data = format_domain_data(data)
                instance_id = data.get('instance_id')
                obj = DomainModel.objects.filter(instance_id=instance_id).first()
                if obj:
                    base_ctl.update_obj(DomainModel, obj.id, data)
                    existed_ids.append(obj.id)
                else:
                    domain_list.append(data)
            if total <= page_num * page_size:
                break
            page_num += 1
        base_ctl.create_objs(DomainModel, domain_list)
        deleted_ids = list(set(set(old_ids) - set(existed_ids)))
        base_ctl.delete_objs(DomainModel, deleted_ids)
    sync_domain_records()


def sync_domain_records():
    '''
    同步域名解析记录
    '''
    with transaction.atomic():
        domain_objs = DomainModel.objects.all()
        old_ids = DomainRecordModel.objects.values_list('id', flat=True).all()
        old_ids = list(set(old_ids))
        existed_ids = []
        record_list = []
        key, secret = aliyun_key_ctl.get_enabled_aliyun_key()
        ali_cli = AliyunDNS(key, secret, 'cn-beijing')
        for domain_obj in domain_objs:
            page_num = 1
            page_size = 50
            while True:
                query = {
                    'domain_name': domain_obj.name,
                    'page_num': page_num,
                    'page_size': page_size,
                }
                data = ali_cli.get_domain_records(**query)
                total = data.get('total')
                data_list = data.get('data_list')
                for data in data_list:
                    instance_id = data.get('RecordId')
                    value = data.get('Value')
                    rr = data.get('RR')
                    typ = data.get('Type')
                    enabled = True if data.get('Status') == 'ENABLE' else False
                    query = {
                        'domain_id': domain_obj.id,
                        'instance_id': instance_id,
                    }
                    obj = DomainRecordModel.objects.filter(**query).first()
                    data = query
                    data['value'] = value
                    data['rr'] = rr
                    data['typ'] = typ
                    # 这里name和fullname就是冗余存储，为了方便查询
                    data['name'] = domain_obj.name
                    data['fullname'] = rr + '.' + domain_obj.name
                    data['enabled'] = enabled
                    if not obj:
                        record_list.append(data)
                    else:
                        base_ctl.update_obj(DomainRecordModel, obj.id, data)
                        existed_ids.append(obj.id)
                if total <= page_num * page_size:
                    break
                page_num += 1
        base_ctl.create_objs(DomainRecordModel, record_list)
        deleted_ids = list(set(set(old_ids) - set(existed_ids)))
        base_ctl.delete_objs(DomainRecordModel, deleted_ids)
    sync_domain_record_asset()


def sync_domain_record_asset():
    '''
    同步解析记录关联的资产
    '''
    with transaction.atomic():
        record_objs = DomainRecordModel.objects.all()
        old_ids = DomainRecordAssetModel.objects.values_list('id', flat=True).all()
        old_ids = list(set(old_ids))
        existed_ids = []
        asset_list = []
        for record_obj in record_objs:
            value = record_obj.value
            # 先查SLB，因为一般情况下肯定是解析到SLB(因为解析到了ECS说明是单点，一般情况下不这么干)
            asset_obj_id = None
            typ = None
            obj = SlbModel.objects.filter(ip=value).first()
            if obj:
                asset_obj_id = obj.id
                typ = DomainRecordAssetModel.TYP_SLB
            else:
                # 只有SLB没有查到时才查ECS
                obj = EcsModel.objects.filter(Q(inner_ip=value)|Q(outer_ip=value)).first()
                if obj:
                    asset_obj_id = obj.id
                    typ = DomainRecordAssetModel.TYP_ECS

            # 现在如果obj存在就说明前面查到了
            if obj:
                query = {
                    'record_id': record_obj.id,
                    'asset_obj_id': asset_obj_id,
                    'typ': typ,
                }
                obj = DomainRecordAssetModel.objects.filter(**query).first()
                data = query
                if not obj:
                    asset_list.append(data)
                else:
                    existed_ids.append(obj.id)
        base_ctl.create_objs(DomainRecordAssetModel, asset_list)
        deleted_ids = list(set(set(old_ids) - set(existed_ids)))
        base_ctl.delete_objs(DomainRecordAssetModel, deleted_ids)
