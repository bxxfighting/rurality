from base.api import BaseApi
from business.service import controllers as service_ctl


class CreateServiceApi(BaseApi):

    need_params = {
        'name': ('名称', 'required str 128'),
        'sign': ('标识', 'required str 128'),
        'project_id': ('项目ID', 'required int'),
        'remark': ('备注', 'optional str 1024'),
    }
    def post(self, request, params):
        data = service_ctl.create_service(**params)
        return data


class UpdateServiceApi(BaseApi):

    need_params = {
        'obj_id': ('服务ID', 'required int'),
        'name': ('名称', 'required str 128'),
        'sign': ('标识', 'required str 128'),
        'project_id': ('项目ID', 'required int'),
        'remark': ('备注', 'optional str 1024'),
    }
    def post(self, request, params):
        data = service_ctl.update_service(**params)
        return data


class DeleteServiceApi(BaseApi):

    need_params = {
        'obj_id': ('服务ID', 'required int'),
    }
    def post(self, request, params):
        data = service_ctl.delete_service(**params)
        return data


class ListServiceApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'keyword': ('关键词', 'optional str 32'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = service_ctl.get_services(**params)
        return data


class ServiceApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('服务ID', 'required int'),
    }

    def post(self, request, params):
        data = service_ctl.get_service(**params)
        return data


class CreateServiceDepartmentApi(BaseApi):

    need_params = {
        'obj_id': ('服务ID', 'required int'),
        'department_id': ('部门ID', 'required int'),
    }
    def post(self, request, params):
        data = service_ctl.create_service_department(**params)
        return data


class DeleteServiceDepartmentApi(BaseApi):

    need_params = {
        'obj_id': ('服务ID', 'required int'),
        'department_id': ('部门ID', 'required int'),
    }
    def post(self, request, params):
        data = service_ctl.delete_service_department(**params)
        return data


class ListServiceDepartmentApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('服务ID', 'required int'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = service_ctl.get_service_departments(**params)
        return data


class CreateServiceUserApi(BaseApi):

    need_params = {
        'obj_id': ('服务ID', 'required int'),
        'user_id': ('用户ID', 'required int'),
        'typ': ('类型', 'required int'),
    }
    def post(self, request, params):
        data = service_ctl.create_service_user(**params)
        return data


class UpdateServiceUserApi(BaseApi):

    need_params = {
        'obj_id': ('服务ID', 'required int'),
        'user_id': ('用户ID', 'required int'),
        'typ': ('类型', 'required int'),
    }
    def post(self, request, params):
        data = service_ctl.update_service_user(**params)
        return data


class DeleteServiceUserApi(BaseApi):

    need_params = {
        'obj_id': ('服务ID', 'required int'),
        'user_id': ('用户ID', 'required int'),
    }
    def post(self, request, params):
        data = service_ctl.delete_service_user(**params)
        return data


class ListServiceUserApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('服务ID', 'required int'),
        'typ': ('类型', 'optional str'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = service_ctl.get_service_users(**params)
        return data
