from random import randint
from django.db import transaction
from django.db.models import Q

from asset.rds.models import RdsModel
from asset.rds.models import RdsAccountModel
from asset.rds.models import RdsDatabaseAccountModel
from base import controllers as base_ctl
from asset.manager.controllers import aliyun_key as aliyun_key_ctl
from utils.aliyun import AliyunRDS
from utils.onlyone import onlyone
from utils.mix import gen_password


def get_accounts(rds_id, keyword=None, page_num=None, page_size=None, operator=None):
    '''
    获取Account列表
    '''
    base_query = RdsAccountModel.objects.filter(rds_id=rds_id)
    if keyword:
        base_query = base_query.filter(username__icontains=keyword)
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


def get_account(obj_id, operator=None):
    '''
    获取Account详情
    '''
    obj = base_ctl.get_obj(RdsAccountModel, obj_id)
    data = obj.to_dict()
    data['rds'] = obj.rds.to_dict()
    return data


@onlyone.lock(RdsAccountModel.model_sign, 'obj_id', 'obj_id', 30)
def update_account(obj_id, password, operator=None):
    '''
    编辑账号
    '''
    data = {
        'password': password,
    }
    obj = base_ctl.update_obj(RdsAccountModel, obj_id, data, operator)
    data = obj.to_dict()
    return data


def get_account_databases(obj_id, page_num=None, page_size=None, operator=None):
    '''
    获取账号关联Database列表
    '''
    base_query = RdsDatabaseAccountModel.objects.filter(account_id=obj_id)
    total = base_query.count()
    objs = base_ctl.query_objs_by_page(base_query, page_num, page_size)
    data_list = []
    for obj in objs:
        data = obj.to_dict()
        data['database'] = obj.database.to_dict()
        data_list.append(data)
    data = {
        'total': total,
        'data_list': data_list,
    }
    return data


def create_account(rds_id, username, remark=''):
    '''
    创建RDS账号
    '''
    rds_obj = base_ctl.get_obj(RdsModel, rds_id)
    key, secret = aliyun_key_ctl.get_enabled_aliyun_key()
    ali_cli = AliyunRDS(key, secret, rds_obj.region_id)
    password = gen_password(level=3, length=randint(8, 32))
    ali_cli.create_account(rds_obj.instance_id, username, password, remark)
