from django.db import transaction

from asset.manager.models import RegionModel
from asset.manager.models import ZoneModel
from base import controllers as base_ctl
from base import errors
from utils.onlyone import onlyone


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
