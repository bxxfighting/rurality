import traceback
from rurality import celery_app

from scheduler.models import BerryModel
from asset.ecs.controllers import sync as ecs_sync
from asset.slb.controllers import sync as slb_sync
from asset.rds.controllers import sync as rds_sync
from asset.redis.controllers import sync as redis_sync
from asset.mongo.controllers import sync as mongo_sync
from asset.rocket.controllers import sync as rocket_sync
from asset.domain.controllers import sync as domain_sync
from base import controllers as base_ctl
from base import errors
from utils import time_utils


@celery_app.task
def apply_task(berry_id):
    try:
        berry_obj = base_ctl.get_obj(BerryModel, berry_id)
        # 一进来就更改任务状态到进行中
        data = {
            'status': BerryModel.ST_RUNNING,
        }
        base_ctl.update_obj(BerryModel, berry_id, data)

        sync_list = ['sync_ecs', 'sync_slb', 'sync_rds', 'sync_redis',
                     'sync_mongo', 'sync_rocket', 'sync_domain']
        # 如果是同步任务，则走此处理方式
        if berry_obj.typ.sign in sync_list:
            sync_task_route(berry_obj)

    except Exception as e:
        # 如果出现异常，则更改任务状态，并且记录错误日志
        log = traceback.format_exc()
        dt_end = time_utils.now()
        duration = dt_end - berry_obj.dt_start
        duration = int(duration.total_seconds())
        data = {
            'status': BerryModel.ST_FAILURE,
            'error_log': log,
            'dt_end': dt_end,
            'duration': duration,
        }
        base_ctl.update_obj(BerryModel, berry_id, data)


def sync_task_route(berry_obj):
    '''
    同步任务
    '''
    if berry_obj.typ.sign == 'sync_ecs':
        ecs_sync.sync_ecses()
    elif berry_obj.typ.sign == 'sync_slb':
        slb_sync.sync_slbs()
    elif berry_obj.typ.sign == 'sync_rds':
        rds_sync.sync_rdses()
    elif berry_obj.typ.sign == 'sync_redis':
        redis_sync.sync_redises()
    elif berry_obj.typ.sign == 'sync_mongo':
        mongo_sync.sync_mongos()
    elif berry_obj.typ.sign == 'sync_domain':
        domain_sync.sync_domains()
    elif berry_obj.typ.sign == 'sync_rocket':
        rocket_sync.sync_rockets()
    else:
        raise errors.CommonError(f'任务{berry_obj.id}: 不存在的任务类型{berry_obj.typ.sign}')
    # 执行成功
    dt_end = time_utils.now()
    duration = dt_end - berry_obj.dt_start
    duration = int(duration.total_seconds())
    data = {
        'status': BerryModel.ST_SUCCESS,
        'dt_end': dt_end,
        'duration': duration,
    }
    base_ctl.update_obj(BerryModel, berry_id, data)
