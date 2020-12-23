from django.db import transaction
from django.db.models import Q

from asset.rds.models import RdsDatabaseModel
from asset.rds.models import RdsDatabaseAccountModel
from base import controllers as base_ctl


def get_databases(rds_id, keyword=None, page_num=None, page_size=None, operator=None):
    '''
    获取Database列表
    '''
    base_query = RdsDatabaseModel.objects.filter(rds_id=rds_id)
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


def get_database(obj_id, operator=None):
    '''
    获取Database详情
    '''
    obj = base_ctl.get_obj(RdsDatabaseModel, obj_id)
    data = obj.to_dict()
    data['rds'] = obj.rds.to_dict()
    return data


def get_database_accounts(obj_id, page_num=None, page_size=None, operator=None):
    '''
    获取Database关联账号列表
    '''
    base_query = RdsDatabaseAccountModel.objects.filter(database_id=obj_id)
    total = base_query.count()
    objs = base_ctl.query_objs_by_page(base_query, page_num, page_size)
    data_list = []
    for obj in objs:
        data = obj.to_dict()
        data['account'] = obj.account.to_dict()
        data_list.append(data)
    data = {
        'total': total,
        'data_list': data_list,
    }
    return data
