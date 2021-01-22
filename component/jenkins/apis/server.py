from base.api import BaseApi
from component.jenkins.controllers import server as server_ctl


class CreateJenkinsServerApi(BaseApi):

    need_params = {
        'name': ('名称', 'required str 128'),
        'host': ('Host', 'required str 128'),
        'username': ('用户名', 'required str 128'),
        'password': ('密码', 'required str 128'),
        'token': ('Token', 'required str 128'),
    }
    def post(self, request, params):
        data = server_ctl.create_jenkins_server(**params)
        return data


class UpdateJenkinsServerApi(BaseApi):

    need_params = {
        'obj_id': ('Jenkins服务ID', 'required int'),
        'name': ('名称', 'required str 128'),
        'host': ('Host', 'required str 128'),
        'username': ('用户名', 'required str 128'),
        'password': ('密码', 'required str 128'),
        'token': ('Token', 'required str 128'),
    }
    def post(self, request, params):
        data = server_ctl.update_jenkins_server(**params)
        return data


class DeleteJenkinsServerApi(BaseApi):

    need_params = {
        'obj_id': ('Jenkins服务ID', 'required int'),
    }
    def post(self, request, params):
        data = server_ctl.delete_jenkins_server(**params)
        return data


class ListJenkinsServerApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = server_ctl.get_jenkins_servers(**params)
        return data


class JenkinsServerApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('Jenkins服务ID', 'required int'),
    }
    def post(self, request, params):
        data = server_ctl.get_jenkins_server(**params)
        return data
