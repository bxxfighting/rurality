from base.api import BaseApi
from asset.slb.controllers import server_group as server_group_ctl


class ServerGroupApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('SLB服务器组ID', 'required int'),
    }
    def post(self, request, params):
        data = server_group_ctl.get_server_group(**params)
        return data


class ListServerGroupApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'slb_id': ('SLB ID', 'optional int'),
        'slb_instance_id': ('SLB实例ID', 'optional str'),
        'keyword': ('关键字', 'optional str'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = server_group_ctl.get_server_groups(**params)
        return data


class ListServerGroupEcsApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('服务器组ID', 'required int'),
        'keyword': ('关键字', 'optional str'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = server_group_ctl.get_server_group_ecses(**params)
        return data


class ListServerGroupServiceApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('服务器组ID', 'required int'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = server_group_ctl.get_server_group_services(**params)
        return data
