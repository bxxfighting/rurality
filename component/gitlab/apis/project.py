from base.api import BaseApi
from component.gitlab.controllers import project as project_ctl


class ListGitlabProjectApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'keyword': ('关键词', 'optional str'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = project_ctl.get_gitlab_projects(**params)
        return data


class SyncGitlabProjectApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
    }
    def post(self, request, params):
        data = project_ctl.sync_gitlab_projects(**params)
        return data
