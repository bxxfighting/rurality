from django.db import transaction
from django.db.models import Q

from asset.slb.models import SlbModel
from scheduler.controllers import berry as berry_ctl
from asset.manager.controllers import aliyun_key as aliyun_key_ctl
from base import controllers as base_ctl


def get_slbs(keyword=None, page_num=None, page_size=None, operator=None):
    '''
    获取SLB列表
    '''
    base_query = SlbModel.objects
    if keyword:
        base_query = base_query.filter(Q(name__icontains=keyword) |
                                       Q(ip__icontains=keyword) |
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


def get_slb(obj_id, operator=None):
    '''
    获取SLB详情
    '''
    obj = base_ctl.get_obj(SlbModel, obj_id)
    data = obj.to_dict()
    return data


def sync_slbs(operator=None):
    '''
    同步SLB
    '''
    # 先进行是否存在阿里云Key判断
    aliyun_key_ctl.get_enabled_aliyun_key()

    params = {}
    data = {
        'name': '同步SLB',
        'typ': 'sync_slb',
        'params': params,
    }
    berry_ctl.create_berry(**data)
