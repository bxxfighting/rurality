from django.db import transaction

from component.jenkins.models import JenkinsServerModel
from account.controllers import user as user_ctl
from base import controllers as base_ctl
from base import errors
from utils.onlyone import onlyone
from utils.jenkins_cli import JenkinsCli


@onlyone.lock(JenkinsServerModel.model_sign, 'name:host', 'host', 30)
@onlyone.lock(JenkinsServerModel.model_sign, 'name', 'name', 30)
def create_jenkins_server(name, host, username, password, token, operator=None):
    '''
    创建Jenkins服务
    '''
    if JenkinsServerModel.objects.filter(name=name).exists():
        raise errors.CommonError('Jenkins已经存在')
    if JenkinsServerModel.objects.filter(host=host).exists():
        raise errors.CommonError('Jenkins已经存在')
    data = {
        'name': name,
        'host': host,
        'username': username,
        'password': password,
        'token': token,
    }
    obj = base_ctl.create_obj(JenkinsServerModel, data, operator)
    data = obj.to_dict()
    return data


@onlyone.lock(JenkinsServerModel.model_sign, 'obj_id:name:host', 'host', 30)
@onlyone.lock(JenkinsServerModel.model_sign, 'obj_id:name', 'name', 30)
@onlyone.lock(JenkinsServerModel.model_sign, 'obj_id', 'obj_id', 30)
def update_jenkins_server(obj_id, name, host, username, password, token, operator=None):
    '''
    编辑Jenkins服务
    '''
    if JenkinsServerModel.objects.filter(name=name).exclude(id=obj_id).exists():
        raise errors.CommonError('Jenkins已经存在')
    if JenkinsServerModel.objects.filter(host=host).exclude(id=obj_id).exists():
        raise errors.CommonError('Jenkins已经存在')
    data = {
        'name': name,
        'host': host,
        'username': username,
        'password': password,
        'token': token,
    }
    obj = base_ctl.update_obj(JenkinsServerModel, obj_id, data, operator)
    data = obj.to_dict()
    return data


@onlyone.lock(JenkinsServerModel.model_sign, 'obj_id', 'obj_id', 30)
def delete_jenkins_server(obj_id, operator=None):
    '''
    删除Jenkins服务
    '''
    base_ctl.delete_obj(JenkinsServerModel, obj_id, operator)


def get_jenkins_servers(page_num=None, page_size=None, operator=None):
    '''
    获取Jenkins服务列表
    '''
    base_query = JenkinsServerModel.objects
    total = base_query.count()
    objs = base_ctl.query_objs_by_page(base_query, page_num, page_size)
    has_password = False
    if operator and user_ctl.has_permission(operator.id, JenkinsServerModel.PASSWORD_PERMISSION):
        has_password = True
    data_list = []
    for obj in objs:
        data = obj.to_dict(has_password=has_password)
        data_list.append(data)
    data = {
        'total': total,
        'data_list': data_list,
    }
    return data


def get_jenkins_server(obj_id, operator=None):
    '''
    获取Jenkins服务
    '''
    obj = base_ctl.get_obj(JenkinsServerModel, obj_id)
    has_password = False
    if operator and user_ctl.has_permission(operator.id, JenkinsServerModel.PASSWORD_PERMISSION):
        has_password = True
    data = obj.to_dict(has_password=has_password)
    return data


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
