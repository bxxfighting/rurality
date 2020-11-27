from base.api import BaseApi
from business.service.controllers import environment as environment_ctl


class CreateEnvironmentApi(BaseApi):

    need_params = {
        'name': ('名称', 'required str 128'),
        'sign': ('标识', 'required str 128'),
        'rank': ('排序值', 'optional int'),
        'remark': ('备注', 'optional str 1024'),
    }
    def post(self, request, params):
        data = environment_ctl.create_environment(**params)
        return data


class UpdateEnvironmentApi(BaseApi):

    need_params = {
        'obj_id': ('环境ID', 'required int'),
        'name': ('名称', 'required str 128'),
        'sign': ('标识', 'required str 128'),
        'rank': ('排序值', 'optional int'),
        'remark': ('备注', 'optional str 1024'),
    }
    def post(self, request, params):
        data = environment_ctl.update_environment(**params)
        return data


class DeleteEnvironmentApi(BaseApi):

    need_params = {
        'obj_id': ('环境ID', 'required int'),
    }
    def post(self, request, params):
        data = environment_ctl.delete_environment(**params)
        return data


class ListEnvironmentApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = environment_ctl.get_environments(**params)
        return data


class EnvironmentApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('环境ID', 'required int'),
    }

    def post(self, request, params):
        data = environment_ctl.get_environment(**params)
        return data
