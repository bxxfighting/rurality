from django.db import transaction
from django.db.models import Q

from business.service.models import ServiceModel
from business.service.models import ServiceEnvironmentModel
from business.service.models import ServiceConfigModel
from business.service.models import EnvironmentModel
from business.service.models import ServiceAssetObjModel
from scheduler.controllers.service import create_service_berry
from base import errors
from base import controllers as base_ctl


def get_service_deploy_config(service_sign, environment_sign):
    '''
    获取服务部署配置
    '''
    service_obj = ServiceModel.objects.filter(sign=service_sign).first()
    if not service_obj:
        raise errors.CommonError('不存在此服务')
    env_obj = EnvironmentModel.objects.filter(sign=environment_sign).first()
    if not env_obj:
        raise errors.CommonError('不存在此环境')
    data = {
        'language': obj.language.sign,
        'frame': obj.frame.sign,
        'gitlab_ssh_url': obj.gitlab.ssh_url,
    }
    query = {
        'service_id': service_obj.id,
        'environment_id': env_obj.id,
    }
    config = ServiceConfigModel.objects.filter(**query).first()
    if not config:
        raise errors.CommonError('此服务不存在对应环境配置')
    data['port'] = config.port
    data['dns_typ'] = config.dns_typ
    data['artifact_typ'] = config.artifact_typ
    data['deploy_typ'] = config.artifact_typ
    return data


def publish_publish(service_id, environment_id, publish_typ, ecs_ids,
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
    ecs_ids = list(set(ecs_ids))
    if publish_typ == 'part' and not ecs_ids:
        raise errors.CommonError('请选择发布机器')
        # 获取服务对应环境所有机器ID
        query = {
            'service_id': service_id,
            'environment_id': environment_id,
            'typ': ServiceAssetObjModel.TYP_ECS,
        }
        existed_ids = ServiceAssetObjModel.objects.filter(**query)\
                .values_list('asset_obj_id', flat=True).all()
        existed_ids = list(set(existed_ids))
        # 正常应该相减为set()空集
        if set(ecs_ids) - set(existed_ids):
            raise errors.CommonError('选择机器异常，请刷新后重新或进行校对')


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
        'ecs_ids': ecs_ids,
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
