from base.api import BaseApi
from scheduler.controllers import berry_type as berry_type_ctl


class CreateBerryTypeApi(BaseApi):

    need_params = {
        'name': ('名称', 'required str 16'),
        'sign': ('标识', 'required str 32'),
        'parent_id': ('父ID', 'optional int'),
    }
    def post(self, request, params):
        data = berry_type_ctl.create_berry_type(**params)
        return data


class UpdateBerryTypeApi(BaseApi):

    need_params = {
        'obj_id': ('任务类型ID', 'required int'),
        'name': ('名称', 'required str 16'),
        'sign': ('标识', 'required str 32'),
        'parent_id': ('父ID', 'optional int'),
    }
    def post(self, request, params):
        data = berry_type_ctl.update_berry_type(**params)
        return data


class DeleteBerryTypeApi(BaseApi):

    need_params = {
        'obj_id': ('任务类型ID', 'required int'),
    }
    def post(self, request, params):
        data = berry_type_ctl.delete_berry_type(**params)
        return data


class ListBerryTypeApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'parent_id': ('父ID', 'optional int'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = berry_type_ctl.get_berry_types(**params)
        return data


class BerryTypeApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('任务类型ID', 'required int'),
    }

    def post(self, request, params):
        data = berry_type_ctl.get_berry_type(**params)
        return data
