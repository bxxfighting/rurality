from django.db import transaction

from asset.manager.models import RegionModel
from asset.manager.models import ZoneModel
from asset.manager.controllers import aliyun_key as aliyun_key_ctl
from base import controllers as base_ctl
from base import errors
from utils.aliyun import AliyunManager


@transaction.atomic
def sync_regions():
    '''
    同步地域
    '''
    key, secret = aliyun_key_ctl.get_enabled_aliyun_key()
    ali_cli = AliyunManager(key, secret, 'cn-beijing')
    regions = ali_cli.get_regions()['data_list']
    data_list = []
    for region in regions:
        instance_id = region.get('RegionId')
        data = {
            'name': region.get('LocalName'),
            'instance_id': instance_id,
            'endpoint': region.get('RegionEndpoint'),
        }
        obj = RegionModel.objects.filter(instance_id=instance_id).first()
        # 存在就更新，不存在就创建
        if obj:
            base_ctl.update_obj(RegionModel, obj.id, data)
        else:
            data_list.append(data)
    base_ctl.create_objs(RegionModel, data_list)


@transaction.atomic
def sync_zones():
    '''
    同步可用区
    '''
    key, secret = aliyun_key_ctl.get_enabled_aliyun_key()
    ali_cli = AliyunManager(key, secret, 'cn-beijing')
    region_objs = RegionModel.objects.all()
    data_list = []
    for region_obj in region_objs:
        zones = ali_cli.get_zones(region_obj.instance_id)['data_list']
        for zone in zones:
            instance_id = zone.get('ZoneId')
            data = {
                'region_id': region_obj.id,
                'name': zone.get('LocalName'),
                'instance_id': instance_id,
            }
            obj = ZoneModel.objects.filter(region_id=region_obj.id, instance_id=instance_id).first()
            # 存在就更新，不存在就创建
            if obj:
                base_ctl.update_obj(ZoneModel, obj.id, data)
            else:
                data_list.append(data)
            data_list.append(data)
    base_ctl.create_objs(ZoneModel, data_list)
