from base.api import BaseApi
from account.controllers import role as role_ctl


class CreateRoleApi(BaseApi):

    need_params = {
        'name': ('名称', 'required str 16'),
        'sign': ('标识', 'required str 32'),
    }
    def post(self, request, params):
        data = role_ctl.create_role(**params)
        return data


class UpdateRoleApi(BaseApi):

    need_params = {
        'obj_id': ('角色ID', 'required int'),
        'name': ('名称', 'required str 16'),
        'sign': ('标识', 'required str 32'),
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
        'keyword': ('关键词', 'optional str 32'),
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


class CreateRoleUserApi(BaseApi):

    need_params = {
        'user_id': ('用户ID', 'required int'),
        'role_id': ('角色ID', 'required int'),
    }
    def post(self, request, params):
        data = role_ctl.create_role_user(**params)
        return data


class DeleteRoleUserApi(BaseApi):

    need_params = {
        'user_id': ('用户ID', 'required int'),
        'role_id': ('角色ID', 'required int'),
    }
    def post(self, request, params):
        data = role_ctl.delete_role_user(**params)
        return data


class ListRoleUserApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('角色ID', 'required int'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = role_ctl.get_role_users(**params)
        return data


class SetRoleModApi(BaseApi):
    '''
    status: create/delete，代表创建或删除
    '''

    need_params = {
        'obj_id': ('角色ID', 'required int'),
        'mod_id': ('模块ID', 'required int'),
        'status': ('状态', 'required str'),
    }
    def post(self, request, params):
        data = role_ctl.set_role_mod(**params)
        return data


class ListRoleModApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('角色ID', 'required int'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = role_ctl.get_role_mods(**params)
        return data


class SetRolePermissionApi(BaseApi):
    '''
    status: create/delete，代表创建或删除
    '''

    need_params = {
        'obj_id': ('角色ID', 'required int'),
        'permission_id': ('权限ID', 'required int'),
        'status': ('状态', 'required str'),
    }
    def post(self, request, params):
        data = role_ctl.set_role_permission(**params)
        return data


class ListRolePermissionApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('角色ID', 'required int'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = role_ctl.get_role_permissions(**params)
        return data


class RoleModPermissionApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('角色ID', 'required int'),
    }

    def post(self, request, params):
        data = role_ctl.get_role_mod_permission(**params)
        return data
