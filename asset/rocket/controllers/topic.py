from django.db import transaction
from django.db.models import Q

from asset.rocket.models import RocketTopicModel
from base import controllers as base_ctl
from base import errors
from utils.onlyone import onlyone


def get_topics(rocket_id=None, rocket_instance_id=None, keyword=None, page_num=None, page_size=None, operator=None):
    '''
    获取Topic列表
    '''
    if not rocket_id and not rocket_instance_id:
        raise errors.CommonError('缺少Rocket ID或Rocket实例ID')
    base_query = RocketTopicModel.objects
    if rocket_id:
        base_query = base_query.filter(rocket_id=rocket_id)
    else:
        base_query = base_query.filter(rocket__instance_id=rocket_instance_id)
    if keyword:
        base_query = base_query.filter(name__icontains=keyword)
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


def get_topic(obj_id, operator=None):
    '''
    获取Topic详情
    '''
    obj = base_ctl.get_obj(RocketTopicModel, obj_id)
    data = obj.to_dict()
    data['rocket'] = obj.rocket.to_dict()
    return data
