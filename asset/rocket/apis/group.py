from base.api import BaseApi
from asset.rocket.controllers import group as group_ctl


class RocketGroupApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('Group ID', 'required int'),
    }
    def post(self, request, params):
        data = group_ctl.get_group(**params)
        return data


class ListRocketGroupApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'rocket_id': ('Rocket ID', 'required int'),
        'keyword': ('关键词', 'optional str'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = group_ctl.get_groups(**params)
        return data
