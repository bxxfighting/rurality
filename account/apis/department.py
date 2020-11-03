from base.api import BaseApi
from account.controllers import department as department_ctl


class CreateDepartmentApi(BaseApi):

    need_params = {
        'name': ('名称', 'required str 16'),
        'sign': ('标识', 'required str 32'),
    }
    def post(self, request, params):
        data = department_ctl.create_department(**params)
        return data


class UpdateDepartmentApi(BaseApi):

    need_params = {
        'obj_id': ('部门ID', 'required int'),
        'name': ('名称', 'required str 16'),
        'sign': ('标识', 'required str 32'),
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
        'keyword': ('关键词', 'optional str 32'),
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


class CreateDepartmentUserApi(BaseApi):

    need_params = {
        'user_id': ('用户ID', 'required int'),
        'department_id': ('部门ID', 'required int'),
        'typ': ('类型', 'required int'),
    }
    def post(self, request, params):
        data = department_ctl.create_department_user(**params)
        return data


class UpdateDepartmentUserApi(BaseApi):

    need_params = {
        'user_id': ('用户ID', 'required int'),
        'department_id': ('部门ID', 'required int'),
        'typ': ('类型', 'required int'),
    }
    def post(self, request, params):
        data = department_ctl.update_department_user(**params)
        return data


class DeleteDepartmentUserApi(BaseApi):

    need_params = {
        'user_id': ('用户ID', 'required int'),
        'department_id': ('部门ID', 'required int'),
    }
    def post(self, request, params):
        data = department_ctl.delete_department_user(**params)
        return data


class ListDepartmentUserApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('部门ID', 'required int'),
        'typ': ('类型', 'optional str'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = department_ctl.get_department_users(**params)
        return data
