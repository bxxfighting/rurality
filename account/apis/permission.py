from base.api import BaseApi
from account.controllers import permission as permission_ctl


class CreatePermissionApi(BaseApi):

    need_params = {
        'mod_id': ('模块ID', 'required int'),
        'name': ('名称', 'required str 6'),
        'sign': ('标识', 'required str 32'),
        'typ': ('类型', 'required int'),
        'rank': ('排序值', 'required int'),
    }
    def post(self, request, params):
        data = permission_ctl.create_permission(**params)
        return data


class UpdatePermissionApi(BaseApi):

    need_params = {
        'obj_id': ('权限ID', 'required int'),
        'name': ('名称', 'required str 6'),
        'sign': ('标识', 'required str 32'),
        'typ': ('类型', 'required int'),
        'rank': ('排序值', 'required int'),
    }
    def post(self, request, params):
        data = permission_ctl.update_permission(**params)
        return data


class DeletePermissionApi(BaseApi):

    need_params = {
        'obj_id': ('权限ID', 'required int'),
    }
    def post(self, request, params):
        data = permission_ctl.delete_permission(**params)
        return data


class ListPermissionApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'mod_id': ('模块ID', 'optional int'),
        'typ': ('类型', 'optional int'),
        'keyword': ('关键字', 'optional str'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = permission_ctl.get_permissions(**params)
        return data


class PermissionApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('权限ID', 'required int'),
    }

    def post(self, request, params):
        data = permission_ctl.get_permission(**params)
        return data
