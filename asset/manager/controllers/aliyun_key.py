from django.db import transaction

from asset.manager.models import AliyunKeyModel
from base import controllers as base_ctl
from base import errors
from utils.onlyone import onlyone


@onlyone.lock(AliyunKeyModel.model_sign, 'key', 'key', 30)
def create_aliyun_key(key, secret, operator):
    '''
    创建阿里云key
    '''
    if AliyunKeyModel.objects.filter(key=key).exists():
        raise errors.CommonError('此Key已经存在')
    data = {
        'key': key,
        'secret': secret,
    }
    obj = base_ctl.create_obj(AliyunKeyModel, data, operator)
    data = obj.to_dict()
    return data


@onlyone.lock(AliyunKeyModel.model_sign, 'obj_id:key', 'key', 30)
@onlyone.lock(AliyunKeyModel.model_sign, 'obj_id', 'obj_id', 30)
def update_aliyun_key(obj_id, key, secret, operator):
    '''
    编辑阿里云key
    '''
    if AliyunKeyModel.objects.filter(key=key).exclude(id=obj_id).exists():
        raise errors.CommonError('此Key已经存在')
    data = {
        'key': key,
        'secret': secret,
    }
    obj = base_ctl.update_obj(AliyunKeyModel, obj_id, data, operator)
    data = obj.to_dict()
    return data


@onlyone.lock(AliyunKeyModel.model_sign, 'obj_id', 'obj_id', 30)
def delete_aliyun_key(obj_id, operator):
    '''
    删除阿里云key
    '''
    obj = base_ctl.get_obj(AliyunKeyModel, obj_id)
    if obj.status == AliyunKeyModel.ST_ENABLE:
        raise errors.CommonError('不允许删除启用状态的Key')
    base_ctl.delete_obj(AliyunKeyModel, obj_id, operator)


def get_aliyun_keys(page_num, page_size, operator):
    '''
    获取阿里云key列表
    '''
    base_query = AliyunKeyModel.objects
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


def get_aliyun_key(obj_id, operator):
    '''
    获取阿里云key
    '''
    obj = base_ctl.get_obj(AliyunKeyModel, obj_id)
    data = obj.to_dict()
    return data


@onlyone.lock(AliyunKeyModel.model_sign, 'obj_id', 'obj_id', 30)
def set_aliyun_key_status(obj_id, status, operator):
    '''
    设置阿里云key状态
    '''
    if not AliyunKeyModel.check_choices('status', status):
        raise errors.CommonError('状态值不正确')
    if status != AliyunKeyModel.ST_ENABLE:
        raise errors.CommonError('暂时只支持启用操作')
    obj = base_ctl.get_obj(AliyunKeyModel, obj_id)
    if obj.status == status:
        return

    with transaction.atomic():
        # 先禁用所有启用状态
        existed_ids = AliyunKeyModel.objects.filter(status=AliyunKeyModel.ST_ENABLE)\
                .values_list('id', flat=True).all()
        data = {
            'status': AliyunKeyModel.ST_DISABLE,
        }
        base_ctl.update_objs(AliyunKeyModel, existed_ids, data)
        # 再启用
        data = {
            'status': status,
        }
        obj = base_ctl.update_obj(AliyunKeyModel, obj_id, data, operator)
    data = obj.to_dict()
    return data


def get_enabled_aliyun_key():
    '''
    获取启用状态的阿里云key
    '''
    obj = AliyunKeyModel.objects.filter(status=AliyunKeyModel.ST_ENABLE).first()
    if not obj:
        raise errors.CommonError('无可用阿里云key')
    return obj.key, obj.secret
