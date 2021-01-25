from django.db import transaction
from django.db.models import Q

from asset.rds.models import RdsAccountModel
from asset.rds.models import RdsDatabaseModel
from asset.rds.models import RdsDatabaseAccountModel
from business.service.models import ServiceAssetObjModel
from business.service.controllers import asset_obj as asset_obj_ctl
from account.controllers import user as user_ctl
from base import controllers as base_ctl
from base import errors


def get_databases(rds_id=None, rds_instance_id=None, keyword=None, page_num=None, page_size=None, operator=None):
    '''
    获取Database列表
    '''
    if not rds_id and not rds_instance_id:
        raise errors.CommonError('缺少RDS ID或RDS实例ID')
    base_query = RdsDatabaseModel.objects
    if rds_id:
        base_query = base_query.filter(rds_id=rds_id)
    else:
        base_query = base_query.filter(rds__instance_id=rds_instance_id)
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
    has_password = False
    if operator and user_ctl.has_permission(operator.id, RdsAccountModel.PASSWORD_PERMISSION):
        has_password = True
    data_list = []
    for obj in objs:
        data = obj.to_dict()
        data['account'] = obj.account.to_dict(has_password=has_password)
        data_list.append(data)
    data = {
        'total': total,
        'data_list': data_list,
    }
    return data


def get_database_services(obj_id, page_num=None, page_size=None, operator=None):
    '''
    获取数据库关联服务列表
    '''
    query = {
        'asset_obj_id': obj_id,
        'typ': ServiceAssetObjModel.TYP_DATABASE,
        'page_num': page_num,
        'page_size': page_size,
    }
    return asset_obj_ctl.get_asset_obj_services(**query)
