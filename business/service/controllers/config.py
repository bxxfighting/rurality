from django.db import transaction
from django.db.models import Q

from base import errors
from base import controllers as base_ctl
from business.service.models import ServiceConfigModel
from utils.onlyone import onlyone


def get_service_config(obj_id, environment_id, operator=None):
    '''
    获取服务配置信息
    '''
    query = {
        'service_id': obj_id,
        'environment_id': environment_id,
    }
    obj = ServiceConfigModel.objects.filter(**query).first()
    if obj:
        data = obj.to_dict()
    else:
        data = ServiceConfigModel.none_to_dict()
    return data


@onlyone.lock(ServiceConfigModel.model_sign, 'obj_id:environment_id', 'obj_id:environment_id', 30)
def update_service_config(obj_id, environment_id, port, dns_typ, artifact_typ, deploy_typ, operator=None):
    '''
    编辑服务配置
    '''
    # TODO: 有关端口号的验证
    if not ServiceConfigModel.check_choices('dns_typ', dns_typ):
        raise errors.CommonError('解析类型不正确')
    if not ServiceConfigModel.check_choices('artifact_typ', artifact_typ):
        raise errors.CommonError('制品类型不正确')
    if not ServiceConfigModel.check_choices('deploy_typ', deploy_typ):
        raise errors.CommonError('部署类型不正确')
    query = {
        'service_id': obj_id,
        'environment_id': environment_id,
    }
    obj = ServiceConfigModel.objects.filter(**query).first()
    data = {
        'service_id': obj_id,
        'environment_id': environment_id,
        'port': port,
        'dns_typ': dns_typ,
        'artifact_typ': artifact_typ,
        'deploy_typ': deploy_typ,
    }
    if obj:
        obj = base_ctl.update_obj(ServiceConfigModel, obj.id, data, operator)
    else:
        obj = base_ctl.create_obj(ServiceConfigModel, data, operator)
    data = obj.to_dict()
    return data
