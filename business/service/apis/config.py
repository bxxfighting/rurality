from base.api import BaseApi
from business.service.controllers import config as config_ctl


class ServiceConfigApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('服务ID', 'required int'),
        'environment_id': ('环境ID', 'required int'),
    }

    def post(self, request, params):
        data = config_ctl.get_service_config(**params)
        return data


class UpdateServiceConfigApi(BaseApi):

    need_params = {
        'obj_id': ('服务ID', 'required int'),
        'environment_id': ('环境ID', 'required int'),
        'port': ('端口号', 'required int'),
        'dns_typ': ('解析类型', 'required str 128'),
        'artifact_typ': ('制品类型', 'required str 128'),
        'deploy_typ': ('部署类型', 'required str 128'),
    }
    def post(self, request, params):
        data = config_ctl.update_service_config(**params)
        return data
