from django.db import transaction

from component.jenkins.models import JenkinsServerModel
from account.controllers import user as user_ctl
from base import controllers as base_ctl
from base import errors
from utils.onlyone import onlyone
from utils.jenkins_cli import JenkinsCli


def get_jenkins_server(operator=None):
    '''
    获取Jenkins服务
    '''
    obj = JenkinsServerModel.objects.first()
    has_password = False
    if operator and user_ctl.has_permission(operator.id, JenkinsServerModel.PASSWORD_PERMISSION):
        has_password = True
    if obj:
        data = obj.to_dict(has_password=has_password)
    else:
        data = JenkinsServerModel.none_to_dict()
    return data


@onlyone.lock(JenkinsServerModel.model_sign, '', '', 30)
def update_jenkins_server(host, username, password, token, operator=None):
    '''
    编辑Jenkins服务配置
    '''
    obj = JenkinsServerModel.objects.first()
    data = {
        'host': host,
        'username': username,
        'password': password,
        'token': token,
    }
    if obj:
        obj = base_ctl.update_obj(JenkinsServerModel, obj.id, data, operator)
    else:
        obj = base_ctl.create_obj(JenkinsServerModel, data, operator)


def get_jenkins_cli():
    '''
    获取Jenkins服务实例
    这里只是简单的获取一个Jenkins实例，
    也就是所有服务、所有环境都使用同一个Jenkins服务
    如果有其它需要可以更改这里的逻辑，比如:
    可以把JenkinsServer和环境关联，不同环境获取不同的Jenkins服务
    '''
    obj = JenkinsServerModel.objects.first()
    if not obj:
        raise errors.CommonError('不存在可用Jenkins服务')
    return JenkinsCli(obj.host, obj.username, obj.token)
