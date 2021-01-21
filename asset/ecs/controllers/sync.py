from django.db import transaction
from django.db.models import Q

from asset.ecs.models import EcsModel
from asset.manager.models import RegionModel
from asset.manager.controllers import aliyun_key as aliyun_key_ctl
from asset.manager.controllers import region as region_ctl
from base import controllers as base_ctl
from base import errors
from utils.aliyun import AliyunECS
from utils.time_utils import str2datetime_by_format


def format_data(data):
    '''
    格式化ECS返回数据
    '''
    name = data.get('InstanceName')
    hostname = data.get('HostName')
    instance_id = data.get('InstanceId')
    inner_ip = ''
    if data.get('InnerIpAddress'):
        if data.get('InnerIpAddress').get('IpAddress'):
            inner_ip = data.get('InnerIpAddress').get('IpAddress')[0]
    if not inner_ip and data.get('NetworkInterfaces'):
        if data.get('NetworkInterfaces').get('NetworkInterface'):
            inner_ip = data.get('NetworkInterfaces').get('NetworkInterface')[0].get('PrimaryIpAddress')

    outer_ip = ''
    if data.get('PublicIpAddress'):
        if data.get('PublicIpAddress').get('IpAddress'):
            outer_ip = data.get('PublicIpAddress').get('IpAddress')[0]
    memory = data.get('Memory')
    cpu = data.get('Cpu')
    os = data.get('OSName')
    charge_typ = data.get('InstanceChargeType')
    region_id = data.get('RegionId')
    zone_id = data.get('ZoneId')
    dt_buy = data.get('CreationTime')
    dt_buy = dt_buy.replace('T', ' ').replace('Z', '')
    dt_buy = str2datetime_by_format(dt_buy, '%Y-%m-%d %H:%M')
    result = {
        'instance_id': instance_id,
        'name': name,
        'hostname': hostname,
        'inner_ip': inner_ip,
        'outer_ip': outer_ip,
        'memory': memory,
        'cpu': cpu,
        'os': os,
        'region_id': region_id,
        'zone_id': zone_id,
        'dt_buy': dt_buy,
        'charge_typ': charge_typ,
    }
    return result


@transaction.atomic
def sync_ecses():
    '''
    同步ECS
    '''
    key, secret = aliyun_key_ctl.get_enabled_aliyun_key()
    regions = region_ctl.get_regions(status=RegionModel.ST_ENABLE)['data_list']
    # 记录原来已经创建过的ECS，用于之后删除已经不存在的使用
    old_ids = EcsModel.objects.values_list('id', flat=True).all()
    old_ids = list(set(old_ids))
    # 用来存储仍然可以查到的ECS
    existed_ids = []
    # 记录需要新创建的ECS信息，用于批量创建
    ecs_list = []
    # 每次使用都先使用默认的地域初始化，其实可以在类里增加默认值，但是没有增加默认值是为了更明确知道在干什么
    ali_cli = AliyunECS(key, secret, 'cn-beijing')
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
            data = ali_cli.get_ecses(**query)
            total = data.get('total')
            data_list = data.get('data_list')
            for data in data_list:
                data = format_data(data)
                instance_id = data.get('instance_id')
                obj = EcsModel.objects.filter(instance_id=instance_id).first()
                if obj:
                    base_ctl.update_obj(EcsModel, obj.id, data)
                    existed_ids.append(obj.id)
                else:
                    ecs_list.append(data)
            if total <= page_num * page_size:
                break
            page_num += 1
    base_ctl.create_objs(EcsModel, ecs_list)
    deleted_ids = list(set(set(old_ids) - set(existed_ids)))
    if deleted_ids:
        base_ctl.delete_objs(EcsModel, deleted_ids)
