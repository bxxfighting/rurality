from django.db import transaction

from asset.manager.models import RegionModel
from asset.manager.models import ZoneModel
from asset.manager.controllers import aliyun_key as aliyun_key_ctl
from base import controllers as base_ctl
from base import errors
from utils.onlyone import onlyone
from utils.aliyun import AliyunManager


def get_regions(status=None, page_num=None, page_size=None, operator=None):
    '''
    获取地域列表
    '''
    base_query = RegionModel.objects
    if status:
        base_query = base_query.filter(status=status)
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


def get_region(obj_id, operator=None):
    '''
    获取地域详情
    '''
    obj = base_ctl.get_obj(RegionModel, obj_id)
    data = obj.to_dict()
    return data


@onlyone.lock(RegionModel.model_sign, 'obj_id', 'obj_id', 30)
def set_region_status(obj_id, status, operator):
    '''
    设置地域状态
    '''
    if not RegionModel.check_choices('status', status):
        raise errors.CommonError('状态值不正确')
    data = {
        'status': status,
    }
    obj = base_ctl.update_obj(RegionModel, obj_id, data)
    data = obj.to_dict()
    return data


def get_zones(region_id, page_num=None, page_size=None, operator=None):
    '''
    获取可用区列表
    '''
    base_query = ZoneModel.objects
    base_query = base_query.filter(region_id=region_id)
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


def get_zone(obj_id, operator=None):
    '''
    获取可用区详情
    '''
    obj = base_ctl.get_obj(ZoneModel, obj_id)
    data = obj.to_dict()
    return data


@transaction.atomic()
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


@transaction.atomic()
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
