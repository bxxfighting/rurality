from django.db import transaction

from asset.vpc.models import VpcModel
from asset.vpc.models import VSwitchModel
from asset.manager.models import RegionModel
from asset.manager.controllers import aliyun_key as aliyun_key_ctl
from asset.manager.controllers import region as region_ctl
from base import controllers as base_ctl
from utils.time_utils import str2datetime_by_format
from utils.aliyun import AliyunVPC


def format_vpc_data(data):
    '''
    格式化VPC返回数据
    '''
    name = data.get('VpcName')
    instance_id = data.get('VpcId')
    cidr_block = data.get('CidrBlock')
    is_default = data.get('IsDefault')
    desc = data.get('Description')
    region_id = data.get('RegionId')
    vswitches = data.get('VSwitchIds').get('VSwitchId')

    result = {
        'instance_id': instance_id,
        'name': name,
        'cidr_block': cidr_block,
        'is_default': is_default,
        'desc': desc,
        'region_id': region_id,
        'vswitch_count': len(vswitches),
    }
    return result


def sync_vpcs():
    '''
    同步VPC
    '''
    with transaction.atomic():
        key, secret = aliyun_key_ctl.get_enabled_aliyun_key()
        regions = region_ctl.get_regions(status=RegionModel.ST_ENABLE)['data_list']
        # 记录原来已经创建过的VPC，用于之后删除已经不存在的使用
        old_ids = VpcModel.objects.values_list('id', flat=True).all()
        old_ids = list(set(old_ids))
        # 用来存储仍然可以查到的VPC
        existed_ids = []
        # 记录需要新创建的VPC信息，用于批量创建
        vpc_list = []
        # 每次使用都先使用默认的地域初始化，其实可以在类里增加默认值，但是没有增加默认值是为了更明确知道在干什么
        ali_cli = AliyunVPC(key, secret, 'cn-beijing')
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
                data = ali_cli.get_vpcs(**query)
                total = data.get('total')
                data_list = data.get('data_list')
                for data in data_list:
                    data = format_vpc_data(data)
                    instance_id = data.get('instance_id')
                    obj = VpcModel.objects.filter(instance_id=instance_id).first()
                    if obj:
                        base_ctl.update_obj(VpcModel, obj.id, data)
                        existed_ids.append(obj.id)
                    else:
                        vpc_list.append(data)
                if total <= page_num * page_size:
                    break
                page_num += 1
        base_ctl.create_objs(VpcModel, vpc_list)
        deleted_ids = list(set(set(old_ids) - set(existed_ids)))
        base_ctl.delete_objs(VpcModel, deleted_ids)


def format_vswitch_data(data):
    result = {
        'name': data.get('VSwitchName'),
        'instance_id': data.get('VSwitchId'),
        'is_default': data.get('IsDefault'),
        'desc': data.get('Description'),
        'cidr_block': data.get('CidrBlock'),
        'zone_id': data.get('ZoneId'),
        'ip_count': data.get('AvailableIpAddressCount'),
    }
    return result


def sync_vswitches():
    '''
    同步交换机
    '''
    with transaction.atomic():
        vpc_objs = VpcModel.objects.all()
        old_ids = VSwitchModel.objects.values_list('id', flat=True).all()
        old_ids = list(set(old_ids))
        existed_ids = []
        vswitch_list = []
        key, secret = aliyun_key_ctl.get_enabled_aliyun_key()
        ali_cli = AliyunVPC(key, secret, 'cn-beijing')
        for vpc_obj in vpc_objs:
            ali_cli.reset_region(vpc_obj.region_id)
            page_num = 1
            page_size = 50
            while True:
                query = {
                    'page_num': page_num,
                    'page_size': page_size,
                    'vpc_instance_id': vpc_obj.instance_id,
                }
                data = ali_cli.get_vswitches(**query)
                data_list = data.get('data_list')
                for data in data_list:
                    data = format_vswitch_data(data)
                    data['region_id'] = vpc_obj.region_id
                    data['vpc_id'] = vpc_obj.id
                    instance_id = data.get('instance_id')
                    query = {
                        'vpc_id': vpc_obj.id,
                        'instance_id': instance_id,
                    }
                    obj = VSwitchModel.objects.filter(**query).first()
                    if not obj:
                        vswitch_list.append(data)
                    else:
                        base_ctl.update_obj(VSwitchModel, obj.id, data)
                        existed_ids.append(obj.id)
                if page_size > len(data_list):
                    break
                page_num += 1
        base_ctl.create_objs(VSwitchModel, vswitch_list)
        deleted_ids = list(set(set(old_ids) - set(existed_ids)))
        base_ctl.delete_objs(VSwitchModel, deleted_ids)
