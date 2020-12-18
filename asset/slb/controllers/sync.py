from django.db import transaction

from asset.ecs.models import EcsModel
from asset.slb.models import SlbModel
from asset.slb.models import SlbServerGroupModel
from asset.slb.models import SlbServerGroupEcsModel
from asset.manager.models import RegionModel
from asset.manager.controllers import aliyun_key as aliyun_key_ctl
from asset.manager.controllers import region as region_ctl
from base import controllers as base_ctl
from utils.time_utils import str2datetime_by_format
from utils.aliyun import AliyunSLB


def format_slb_data(data):
    '''
    格式化SLB返回数据
    '''
    name = data.get('LoadBalancerName')
    instance_id = data.get('LoadBalancerId')
    ip = data.get('Address')
    ip_typ = data.get('AddressType')
    zone_id = data.get('MasterZoneId')
    slave_zone_id = data.get('SlaveZoneId')
    region_id = data.get('RegionId')
    dt_buy = data.get('CreateTime')
    dt_buy = dt_buy.replace('T', ' ').replace('Z', '')
    dt_buy = str2datetime_by_format(dt_buy, '%Y-%m-%d %H:%M')
    result = {
        'name': name,
        'instance_id': instance_id,
        'ip': ip,
        'ip_typ': ip_typ,
        'zone_id': zone_id,
        'slave_zone_id': slave_zone_id,
        'region_id': region_id,
        'dt_buy': dt_buy,
    }
    return result


def sync_slbs():
    '''
    同步SLB
    '''
    with transaction.atomic():
        key, secret = aliyun_key_ctl.get_enabled_aliyun_key()
        regions = region_ctl.get_regions(status=RegionModel.ST_ENABLE)['data_list']
        # 记录原来已经创建过的SLB，用于之后删除已经不存在的使用
        old_ids = SlbModel.objects.values_list('id', flat=True).all()
        old_ids = list(set(old_ids))
        # 用来存储仍然可以查到的SLB
        existed_ids = []
        # 记录需要新创建的SLB信息，用于批量创建
        slb_list = []
        # 每次使用都先使用默认的地域初始化，其实可以在类里增加默认值，但是没有增加默认值是为了更明确知道在干什么
        ali_cli = AliyunSLB(key, secret, 'cn-beijing')
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
                data = ali_cli.get_slbs(**query)
                total = data.get('total')
                data_list = data.get('data_list')
                for data in data_list:
                    data = format_slb_data(data)
                    instance_id = data.get('instance_id')
                    obj = SlbModel.objects.filter(instance_id=instance_id).first()
                    if obj:
                        base_ctl.update_obj(SlbModel, obj.id, data)
                        existed_ids.append(obj.id)
                    else:
                        slb_list.append(data)
                if total <= page_num * page_size:
                    break
                page_num += 1
        base_ctl.create_objs(SlbModel, slb_list)
        deleted_ids = list(set(set(old_ids) - set(existed_ids)))
        if deleted_ids:
            base_ctl.delete_objs(SlbModel, deleted_ids)
    sync_slb_backend_servers()


def sync_slb_backend_servers():
    '''
    同步SLB默认服务器组服务器
    '''
    with transaction.atomic():
        slb_objs = SlbModel.objects.all()
        query = {
            'server_group__typ': SlbServerGroupModel.TYP_DEFAULT,
        }
        old_ids = SlbServerGroupEcsModel.objects.filter(**query).values_list('id', flat=True).all()
        old_ids = list(set(old_ids))
        existed_ids = []
        ecs_list = []
        key, secret = aliyun_key_ctl.get_enabled_aliyun_key()
        ali_cli = AliyunSLB(key, secret, 'cn-beijing')
        for slb_obj in slb_objs:
            group_obj = SlbServerGroupModel.objects.filter(slb_id=slb_obj.id)\
                    .filter(typ=SlbServerGroupModel.TYP_DEFAULT).first()
            if not group_obj:
                data = {
                    'slb_id': slb_obj.id,
                    'name': 'default',
                    'instance_id': 'default',
                    'typ': SlbServerGroupModel.TYP_DEFAULT,
                }
                group_obj = base_ctl.create_obj(SlbServerGroupModel, data)
            ali_cli.reset_region(slb_obj.region_id)
            ecses = ali_cli.get_slb_info(slb_obj.instance_id).get('backend_servers')
            for ecs in ecses:
                ecs_instance_id = ecs.get('ServerId')
                ecs_obj = EcsModel.objects.filter(instance_id=ecs_instance_id).first()
                weight = ecs.get('Weight')
                obj = SlbServerGroupEcsModel.objects.filter(slb_id=slb_obj.id)\
                        .filter(server_group_id=group_obj.id, ecs_id=ecs_obj.id).first()
                data = {
                    'slb_id': slb_obj.id,
                    'server_group_id': group_obj.id,
                    'ecs_id': ecs_obj.id,
                    'weight': weight,
                }
                if not obj:
                    ecs_list.append(data)
                else:
                    base_ctl.update_obj(SlbServerGroupEcsModel, obj.id, data)
                    existed_ids.append(obj.id)
        base_ctl.create_objs(SlbServerGroupEcsModel, ecs_list)
        deleted_ids = list(set(set(old_ids) - set(existed_ids)))
        if deleted_ids:
            base_ctl.delete_objs(SlbServerGroupEcsModel, deleted_ids)
    sync_slb_vserver_groups()


def sync_slb_vserver_groups():
    '''
    同步SLB虚拟服务器组
    '''
    with transaction.atomic():
        slb_objs = SlbModel.objects.all()
        old_ids = SlbServerGroupModel.objects.filter(typ=SlbServerGroupModel.TYP_VSERVER)\
                .values_list('id', flat=True).all()
        old_ids = list(set(old_ids))
        existed_ids = []
        group_list = []
        key, secret = aliyun_key_ctl.get_enabled_aliyun_key()
        ali_cli = AliyunSLB(key, secret, 'cn-beijing')
        for slb_obj in slb_objs:
            ali_cli.reset_region(slb_obj.region_id)
            groups = ali_cli.get_vserver_groups(slb_obj.instance_id).get('data_list')
            for group in groups:
                group_instance_id = group.get('VServerGroupId')
                group_name = group.get('VServerGroupName')
                query = {
                    'slb_id': slb_obj.id,
                    'typ': SlbServerGroupModel.TYP_VSERVER,
                    'instance_id': group_instance_id,
                }
                group_obj = SlbServerGroupModel.objects.filter(**query).first()
                data = {
                    'slb_id': slb_obj.id,
                    'instance_id': group_instance_id,
                    'name': group_name,
                    'typ': SlbServerGroupModel.TYP_VSERVER,
                }
                if not group_obj:
                    group_list.append(data)
                else:
                    group_obj = base_ctl.update_obj(SlbServerGroupModel, group_obj.id, data)
                    existed_ids.append(group_obj.id)
        base_ctl.create_objs(SlbServerGroupModel, group_list)
        deleted_ids = list(set(set(old_ids) - set(existed_ids)))
        if deleted_ids:
            base_ctl.delete_objs(SlbServerGroupModel, deleted_ids)
    sync_slb_vserver_group_backend_servers()


def sync_slb_vserver_group_backend_servers():
    '''
    同步虚拟服务器组后端服务器
    '''
    with transaction.atomic():
        query = {
            'typ': SlbServerGroupModel.TYP_VSERVER,
        }
        group_objs = SlbServerGroupModel.objects.filter(**query).all()

        query = {
            'server_group__typ': SlbServerGroupModel.TYP_VSERVER,
        }
        old_ids = SlbServerGroupEcsModel.objects.filter(**query).values_list('id', flat=True).all()
        old_ids = list(set(old_ids))
        existed_ids = []
        ecs_list = []
        key, secret = aliyun_key_ctl.get_enabled_aliyun_key()
        ali_cli = AliyunSLB(key, secret, 'cn-beijing')
        for group_obj in group_objs:
            ali_cli.reset_region(group_obj.slb.region_id)
            ecses = ali_cli.get_vserver_group_backend_servers(group_obj.instance_id).get('data_list')
            for ecs in ecses:
                ecs_instance_id = ecs.get('ServerId')
                weight = ecs.get('Weight')
                ecs_obj = EcsModel.objects.filter(instance_id=ecs_instance_id).first()
                query = {
                    'slb_id': group_obj.slb_id,
                    'server_group_id': group_obj.id,
                    'ecs_id': ecs_obj.id,
                }
                obj = SlbServerGroupEcsModel.objects.filter(**query).first()
                data = {
                    'slb_id': group_obj.slb_id,
                    'server_group_id': group_obj.id,
                    'ecs_id': ecs_obj.id,
                    'weight': weight,
                }
                if not obj:
                    ecs_list.append(data)
                else:
                    base_ctl.update_obj(SlbServerGroupEcsModel, obj.id, data)
                    existed_ids.append(obj.id)
        base_ctl.create_objs(SlbServerGroupEcsModel, ecs_list)
        deleted_ids = list(set(set(old_ids) - set(existed_ids)))
        if deleted_ids:
            base_ctl.delete_objs(SlbServerGroupEcsModel, deleted_ids)
