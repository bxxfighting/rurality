from django.db import transaction

from base import errors
from utils import time_utils


def get_obj(obj_model, obj_id):
    obj = obj_model.objects.filter(id=obj_id).first()
    if not obj:
        raise errors.CommonError('{}不存在'.format(obj_model.model_name))
    return obj


def get_obj_or_none(obj_model, obj_id):
    obj = obj_model.objects.filter(id=obj_id).first()
    return obj


def query_objs_by_page(base_query, page_num=None, page_size=None):
    '''
    用于对查询结果进行分页
    如果有排序需求，需要在base_query上直接处理后，再传参
    '''
    objs = base_query.all()
    if page_num and page_size:
        end = page_num * page_size
        start = end - page_size
        objs = objs[start:end]
    return objs


@transaction.atomic()
def create_obj(obj_model, data, operator=None):
    '''
    创建对象
    '''
    obj = obj_model.objects.create(**data)
    return obj


@transaction.atomic()
def create_objs(obj_model, data_list, operator=None):
    '''
    批量创建对象
    '''
    obj_list = []
    for data in data_list:
        obj_list.append(obj_model(**data))
        if len(obj_list) >= 2000:
            obj_model.objects.bulk_create(obj_list)
            obj_list = []
    if obj_list:
        obj_model.objects.bulk_create(obj_list)


@transaction.atomic()
def update_obj(obj_model, obj_id, data, operator=None):
    '''
    更新对象
    '''
    obj = get_obj(obj_model, obj_id)
    change_list = []
    for key, value in data.items():
        new_value = value
        old_value = getattr(obj, key)
        if new_value != old_value:
            change_data = {
                'key': key,
                'name': obj_model.field_verbose_name(key),
                'old_value': old_value,
                'new_value': new_value,
            }
            change_list.append(change_data)
            setattr(obj, key, new_value)
    if change_list:
        obj.dt_update = time_utils.now()
        obj.save()
    return obj


@transaction.atomic()
def update_objs(obj_model, obj_ids, data, operator=None):
    '''
    批量更新
    '''
    data['dt_update'] = time_utils.now()
    obj_model.objects.filter(id__in=list(obj_ids)).update(**data)


@transaction.atomic()
def delete_obj(obj_model, obj_id, operator=None):
    '''
    删除对象
    '''
    obj = get_obj(obj_model, obj_id)
    obj.is_deleted = True
    obj.dt_update = time_utils.now()
    obj.save()
    return obj


def delete_objs(obj_model, obj_ids, operator=None):
    '''
    批量删除对象
    '''
    if not obj_ids:
        return
    data = {
        'is_deleted': True,
        'dt_update': time_utils.now(),
    }
    obj_model.objects.filter(id__in=list(obj_ids)).update(**data)
