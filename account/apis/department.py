from base.api import BaseApi
from account.controllers import department as department_ctl


class CreateDepartmentApi(BaseApi):

    need_params = {
        'name': ('名称', 'required str 16'),
        'sign': ('标识', 'required str 16'),
    }
    def post(self, request, params):
        data = department_ctl.create_department(**params)
        return data


class UpdateDepartmentApi(BaseApi):

    need_params = {
        'obj_id': ('部门ID', 'required int'),
        'name': ('名称', 'required str 16'),
        'sign': ('标识', 'required str 16'),
    }
    def post(self, request, params):
        data = department_ctl.update_department(**params)
        return data


class DeleteDepartmentApi(BaseApi):

    need_params = {
        'obj_id': ('部门ID', 'required int'),
    }
    def post(self, request, params):
        data = department_ctl.delete_department(**params)
        return data


class ListDepartmentApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'keyword': ('关键词', 'optional str 16'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = department_ctl.get_departments(**params)
        return data


class DepartmentApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('部门ID', 'required int'),
    }

    def post(self, request, params):
        data = department_ctl.get_department(**params)
        return data
