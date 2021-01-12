from django.db import transaction
from django.db.models import Q

from scheduler.models import BerryTypeModel
from scheduler.models import BerryModel
from scheduler.tasks import berry as berry_tasks
from base import controllers as base_ctl
from base import errors
from utils import time_utils


def create_berry(name, typ, time_mode=BerryModel.TIME_MODE_NOW, dt_start=None, params={}, operator=None):
    '''
    创建任务
    params: dict
    '''
    query = {
        'sign': typ,
    }
    typ_obj = BerryTypeModel.objects.filter(**query).first()
    if not typ_obj:
        raise errors.CommonError('任务类型不存在')
    if not BerryModel.check_choices('time_mode', time_mode):
        raise errors.CommonError('时间模式值不正确')

    now = time_utils.now()
    countdown = 0
    if time_mode == BerryModel.TIME_MODE_CRONTAB:
        if not dt_start:
            raise errors.CommonError('定时任务必须传开始时间')
        if dt_start <= now:
            raise errors.CommonError('不能指定过去的时间')
        countdown = dt_start - now
        countdown = int(countdown.total_seconds())
        if countdown < 5 * 60:
            raise errors.CommonError('定时任务必须指定五分钟以后的时间')
    else:
        dt_start = time_utils.now()

    data = {
        'name': name,
        'typ_id': typ_obj.id,
        'time_mode': time_mode,
        'dt_start': dt_start,
        'input_params': params,
    }
    berry_obj = base_ctl.create_obj(BerryModel, data)
    result = berry_tasks.apply_task.apply_async(countdown=countdown, args=[berry_obj.id])
    data = {
        'task_id': result.task_id,
    }
    base_ctl.update_obj(BerryModel, berry_obj.id, data)
