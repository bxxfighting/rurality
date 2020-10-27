from base.api import BaseApi
from account.controllers import role as role_ctl


class CreateRoleApi(BaseApi):

    need_params = {
        'name': ('名称', 'required str 16'),
        'sign': ('标识', 'required str 16'),
    }
    def post(self, request, params):
        data = role_ctl.create_role(**params)
        return data


class UpdateRoleApi(BaseApi):

    need_params = {
        'obj_id': ('角色ID', 'required int'),
        'name': ('名称', 'required str 16'),
        'sign': ('标识', 'required str 16'),
    }
    def post(self, request, params):
        data = role_ctl.update_role(**params)
        return data


class DeleteRoleApi(BaseApi):

    need_params = {
        'obj_id': ('角色ID', 'required int'),
    }
    def post(self, request, params):
        data = role_ctl.delete_role(**params)
        return data


class ListRoleApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'keyword': ('关键词', 'optional str 16'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = role_ctl.get_roles(**params)
        return data


class RoleApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('角色ID', 'required int'),
    }

    def post(self, request, params):
        data = role_ctl.get_role(**params)
        return data
