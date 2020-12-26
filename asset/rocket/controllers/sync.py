import ujson as json
from django.db import transaction

from asset.rocket.models import RocketModel
from asset.rocket.models import RocketTopicModel
from asset.rocket.models import RocketGroupModel
from asset.manager.models import RegionModel
from asset.manager.controllers import aliyun_key as aliyun_key_ctl
from asset.manager.controllers import region as region_ctl
from base import controllers as base_ctl
from utils.aliyun import AliyunONS


def format_rocket_data(data):
    '''
    格式化Rocket返回数据
    '''
    instance_id = data.get('InstanceId')
    name = data.get('InstanceName')
    is_independent_naming = data.get('IndependentNaming')

    result = {
    	'instance_id': instance_id,
    	'name': name,
    	'is_independent_naming': is_independent_naming,
    }
    return result


def sync_rockets():
    '''
    同步Rocket
    '''
    with transaction.atomic():
        key, secret = aliyun_key_ctl.get_enabled_aliyun_key()
        regions = region_ctl.get_regions(status=RegionModel.ST_ENABLE)['data_list']
        # 记录原来已经创建过的Rocket，用于之后删除已经不存在的使用
        old_ids = RocketModel.objects.values_list('id', flat=True).all()
        old_ids = list(set(old_ids))
        # 用来存储仍然可以查到的Rocket
        existed_ids = []
        # 记录需要新创建的Rocket信息，用于批量创建
        rocket_list = []
        # 每次使用都先使用默认的地域初始化，其实可以在类里增加默认值，但是没有增加默认值是为了更明确知道在干什么
        ali_cli = AliyunONS(key, secret, 'cn-beijing')
        for region in regions:
            region_id = region.get('instance_id')
            ali_cli.reset_region(region_id)
            data = ali_cli.get_rockets()
            total = data.get('total')
            data_list = data.get('data_list')
            for data in data_list:
                data = format_rocket_data(data)
                data['region_id'] = region_id
                instance_id = data.get('instance_id')
                obj = RocketModel.objects.filter(instance_id=instance_id).first()
                if obj:
                    base_ctl.update_obj(RocketModel, obj.id, data)
                    existed_ids.append(obj.id)
                else:
                    rocket_list.append(data)
        base_ctl.create_objs(RocketModel, rocket_list)
        deleted_ids = list(set(set(old_ids) - set(existed_ids)))
        base_ctl.delete_objs(RocketModel, deleted_ids)
    sync_rocket_topics()


def sync_rocket_topics():
    '''
    同步Rocket账号
    '''
    with transaction.atomic():
        rocket_objs = RocketModel.objects.all()
        old_ids = RocketTopicModel.objects.values_list('id', flat=True).all()
        old_ids = list(set(old_ids))
        existed_ids = []
        topic_list = []
        key, secret = aliyun_key_ctl.get_enabled_aliyun_key()
        ali_cli = AliyunONS(key, secret, 'cn-beijing')
        for rocket_obj in rocket_objs:
            ali_cli.reset_region(rocket_obj.region_id)
            query = {
                'instance_id': rocket_obj.instance_id,
            }
            data = ali_cli.get_rocket_topics(**query)
            data_list = data.get('data_list')
            for data in data_list:
                name = data.get('Topic')
                remark = data.get('Remark')
                query = {
                    'rocket_id': rocket_obj.id,
                    'name': name,
                }
                obj = RocketTopicModel.objects.filter(**query).first()
                data = query
                data['remark'] = remark
                if not obj:
                    topic_list.append(data)
                else:
                    base_ctl.update_obj(RocketTopicModel, obj.id, data)
                    existed_ids.append(obj.id)
        base_ctl.create_objs(RocketTopicModel, topic_list)
        deleted_ids = list(set(set(old_ids) - set(existed_ids)))
        base_ctl.delete_objs(RocketTopicModel, deleted_ids)
    sync_rocket_groups()


def sync_rocket_groups():
    '''
    同步Rocket Group
    '''
    with transaction.atomic():
        rocket_objs = RocketModel.objects.all()
        old_ids = RocketGroupModel.objects.values_list('id', flat=True).all()
        old_ids = list(set(old_ids))
        existed_ids = []
        group_list = []
        key, secret = aliyun_key_ctl.get_enabled_aliyun_key()
        ali_cli = AliyunONS(key, secret, 'cn-beijing')
        for rocket_obj in rocket_objs:
            ali_cli.reset_region(rocket_obj.region_id)
            query = {
                'instance_id': rocket_obj.instance_id,
            }
            data = ali_cli.get_rocket_groups(**query)
            data_list = data.get('data_list')
            for data in data_list:
                name = data.get('GroupId')
                typ = data.get('GroupType')
                remark = data.get('Remark')
                query = {
                    'rocket_id': rocket_obj.id,
                    'name': name,
                }
                obj = RocketGroupModel.objects.filter(**query).first()
                data = query
                data['typ'] = typ
                data['remark'] = remark
                if not obj:
                    group_list.append(data)
                else:
                    base_ctl.update_obj(RocketGroupModel, obj.id, data)
                    existed_ids.append(obj.id)
        base_ctl.create_objs(RocketGroupModel, group_list)
        deleted_ids = list(set(set(old_ids) - set(existed_ids)))
        base_ctl.delete_objs(RocketGroupModel, deleted_ids)
