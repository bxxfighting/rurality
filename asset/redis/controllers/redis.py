from django.db import transaction
from django.db.models import Q

from asset.redis.models import RedisModel
from base import controllers as base_ctl


def get_redises(keyword=None, page_num=None, page_size=None, operator=None):
    '''
    获取Redis列表
    '''
    base_query = RedisModel.objects
    if keyword:
        base_query = base_query.filter(Q(name__icontains=keyword) |
                                       Q(connection__icontains=keyword) |
                                       Q(instance_id__icontains=keyword))
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


def get_redis(obj_id, operator=None):
    '''
    获取Redis详情
    '''
    obj = base_ctl.get_obj(RedisModel, obj_id)
    data = obj.to_dict()
    return data
