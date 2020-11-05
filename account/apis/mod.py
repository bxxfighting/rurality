from base.api import BaseApi
from account.controllers import mod as mod_ctl


class CreateModApi(BaseApi):

    need_params = {
        'name': ('名称', 'required str 16'),
        'sign': ('标识', 'required str 16'),
        'rank': ('排序值', 'required int'),
    }
    def post(self, request, params):
        data = mod_ctl.create_mod(**params)
        return data


class UpdateModApi(BaseApi):

    need_params = {
        'obj_id': ('模块ID', 'required int'),
        'name': ('名称', 'required str 16'),
        'sign': ('标识', 'required str 16'),
        'rank': ('排序值', 'required int'),
    }
    def post(self, request, params):
        data = mod_ctl.update_mod(**params)
        return data


class DeleteModApi(BaseApi):

    need_params = {
        'obj_id': ('模块ID', 'required int'),
    }
    def post(self, request, params):
        data = mod_ctl.delete_mod(**params)
        return data


class ListModApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'keyword': ('关键词', 'optional str 16'),
        'need_permission': ('是否返回权限', 'optional bool'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = mod_ctl.get_mods(**params)
        return data


class ModApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('模块ID', 'required int'),
    }

    def post(self, request, params):
        data = mod_ctl.get_mod(**params)
        return data
