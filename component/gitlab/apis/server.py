from base.api import BaseApi
from component.gitlab.controllers import server as server_ctl


class UpdateGitlabServerApi(BaseApi):

    need_params = {
        'host': ('Host', 'required str 128'),
        'username': ('用户名', 'required str 128'),
        'password': ('密码', 'required str 128'),
        'token': ('Token', 'required str 128'),
    }
    def post(self, request, params):
        server_ctl.update_gitlab_server(**params)


class GitlabServerApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
    }
    def get(self, request, params):
        data = server_ctl.get_gitlab_server(**params)
        return data
