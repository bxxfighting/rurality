from django.db import transaction
from django.db.models import Q

from asset.rocket.models import RocketGroupModel
from base import controllers as base_ctl
from utils.onlyone import onlyone


def get_groups(rocket_id, keyword=None, page_num=None, page_size=None, operator=None):
    '''
    获取Group列表
    '''
    base_query = RocketGroupModel.objects.filter(rocket_id=rocket_id)
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


def get_group(obj_id, operator=None):
    '''
    获取Group详情
    '''
    obj = base_ctl.get_obj(RocketGroupModel, obj_id)
    data = obj.to_dict()
    data['rocket'] = obj.rocket.to_dict()
    return data
