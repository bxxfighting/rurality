from base.api import BaseApi
from component.jenkins.controllers import job as job_ctl


class ListJenkinsJobApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'server_id': ('Jenkins服务ID', 'optional int'),
        'keyword': ('关键词', 'optional str'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = job_ctl.get_jenkins_jobs(**params)
        return data


class SyncJenkinsJobApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
    }
    def post(self, request, params):
        data = job_ctl.sync_jenkins_jobs(**params)
        return data
