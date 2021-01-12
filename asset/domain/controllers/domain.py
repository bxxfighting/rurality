from django.db import transaction
from django.db.models import Q

from asset.domain.models import DomainModel
from scheduler.controllers import berry as berry_ctl
from asset.manager.controllers import aliyun_key as aliyun_key_ctl
from base import controllers as base_ctl


def get_domains(keyword=None, page_num=None, page_size=None, operator=None):
    '''
    获取域名列表
    '''
    base_query = DomainModel.objects
    if keyword:
        base_query = base_query.filter(Q(name__icontains=keyword) |
                                       Q(instance_id__icontains=keyword))
    total = base_query.count()
    # 按解析数量倒序排列，解析多，说明更频繁查看
    base_query = base_query.order_by('-record_count')
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


def get_domain(obj_id, operator=None):
    '''
    获取域名详情
    '''
    obj = base_ctl.get_obj(DomainModel, obj_id)
    data = obj.to_dict()
    return data


def sync_domains(operator=None):
    '''
    同步域名
    '''
    aliyun_key_ctl.get_enabled_aliyun_key()
    params = {}
    data = {
        'name': '同步域名',
        'typ': 'sync_domain',
        'params': params,
    }
    berry_ctl.create_berry(**data)
