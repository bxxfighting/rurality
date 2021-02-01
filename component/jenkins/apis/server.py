from base.api import BaseApi
from component.jenkins.controllers import server as server_ctl


class UpdateJenkinsServerApi(BaseApi):

    need_params = {
        'name': ('名称', 'required str 128'),
        'host': ('Host', 'required str 128'),
        'username': ('用户名', 'required str 128'),
        'password': ('密码', 'required str 128'),
        'token': ('Token', 'required str 128'),
    }
    def post(self, request, params):
        server_ctl.update_jenkins_server(**params)


class JenkinsServerApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('Jenkins服务ID', 'required int'),
    }
    def get(self, request, params):
        data = server_ctl.get_jenkins_server(**params)
        return data
