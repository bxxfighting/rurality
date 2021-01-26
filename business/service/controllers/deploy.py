from django.db import transaction
from django.db.models import Q

from business.service.models import ServiceModel
from business.service.models import ServiceEnvironmentModel
from business.service.models import EnvironmentModel
from scheduler.controllers.service import create_service_berry
from base import errors
from base import controllers as base_ctl


def publish_publish(service_id, environment_id, publish_typ, hosts,
        version_typ, version, time_mode, dt_start, operator=None):
    '''
    服务发布
    publish_typ: full(全量发布)/part(部分发布)
    version_typ: tag(按Tag号发布)/branch(按分支发布)
    version: tag号或者分支名
    '''
    publish_typ_choices = ('full', 'part')
    version_typ_choices = ('tag', 'branch')

    if publish_typ not in publish_typ_choices:
        raise errors.CommonError('发布类型不存在')
    if version_typ not in version_typ_choices:
        raise errors.CommonError('版本类型不存在')
    # TODO: 调用gitlab接口, 验证version是否存在

    service_obj = base_ctl.get_obj(ServiceModel, service_id)
    environment_obj = base_ctl.get_obj(EnvironmentModel, service_id)
    query = {
        'service_id': service_id,
        'environment_id': environment_id,
    }
    if not ServiceEnvironmentModel.objects.filter(**query).exists():
        raise errors.CommonError('服务不存在对应环境')

    input_params = {
        'publish_typ': publish_typ,
        'version_typ': version_typ,
        'version': version,
    }

    name = f'{service_obj.name}-{environment_obj.name}-发布-{version}'
    data = {
        'name': name,
        'service_id': service_id,
        'environment_id': environment_id,
        'typ': 'service_publish',
        'time_mode': time_mode,
        'dt_start': dt_start,
        'input_params': input_params,
        'operator': operator,
    }
    create_service_berry(**data)


def restart_service(service_id, environment_id, publish_typ, hosts,
        time_mode, dt_start, operator=None):
    '''
    服务重启
    '''
    service_obj = base_ctl.get_obj(ServiceModel, service_id)
    environment_obj = base_ctl.get_obj(EnvironmentModel, service_id)
    query = {
        'service_id': service_id,
        'environment_id': environment_id,
    }
    if not ServiceEnvironmentModel.objects.filter(**query).exists():
        raise errors.CommonError('服务不存在对应环境')

    input_params = {}

    name = f'{service_obj.name}-{environment_obj.name}-重启'
    data = {
        'name': name,
        'service_id': service_id,
        'environment_id': environment_id,
        'typ': 'service_restart',
        'time_mode': time_mode,
        'dt_start': dt_start,
        'input_params': input_params,
        'operator': operator,
    }
    create_service_berry(**data)


def rollback_service(service_id, environment_id, publish_typ, hosts,
        version, time_mode, dt_start, operator=None):
    '''
    服务回滚
    version: 制品版本(回滚以制品的概念回滚)
    '''
    # TODO: 调用对应制品接口, 验证version是否存在

    service_obj = base_ctl.get_obj(ServiceModel, service_id)
    environment_obj = base_ctl.get_obj(EnvironmentModel, service_id)
    query = {
        'service_id': service_id,
        'environment_id': environment_id,
    }
    if not ServiceEnvironmentModel.objects.filter(**query).exists():
        raise errors.CommonError('服务不存在对应环境')

    input_params = {
        'version': version,
    }

    name = f'{service_obj.name}-{environment_obj.name}-回滚-{version}'
    data = {
        'name': name,
        'service_id': service_id,
        'environment_id': environment_id,
        'typ': 'service_rollback',
        'time_mode': time_mode,
        'dt_start': dt_start,
        'input_params': input_params,
        'operator': operator,
    }
    create_service_berry(**data)
