from django.db import transaction

from component.gitlab.models import GitlabServerModel
from account.controllers import user as user_ctl
from base import controllers as base_ctl
from base import errors
from utils.onlyone import onlyone


def get_gitlab_server(operator=None):
    '''
    获取Gitlab服务配置信息
    '''
    obj = GitlabServerModel.objects.first()
    has_password = False
    if operator and user_ctl.has_permission(operator.id, GitlabServerModel.PASSWORD_PERMISSION):
        has_password = True
    if obj:
        data = obj.to_dict(has_password=has_password)
    else:
        data = GitlabServerModel.none_to_dict()
    return data


@onlyone.lock(GitlabServerModel.model_sign, '', '', 30)
def update_gitlab_server(host, username, password, token, operator=None):
    '''
    编辑Gitlab服务配置
    '''
    obj = GitlabServerModel.objects.first()
    data = {
        'host': host,
        'username': username,
        'password': password,
        'token': token,
    }
    if obj:
        obj = base_ctl.update_obj(GitlabServerModel, obj.id, data, operator)
    else:
        obj = base_ctl.create_obj(GitlabServerModel, data, operator)
