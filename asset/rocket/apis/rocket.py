from base.api import BaseApi
from asset.rocket.controllers import rocket as rocket_ctl


class RocketApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('Rocket ID', 'required int'),
    }
    def post(self, request, params):
        data = rocket_ctl.get_rocket(**params)
        return data


class ListRocketApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'keyword': ('关键字', 'optional str'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = rocket_ctl.get_rockets(**params)
        return data


class SyncRocketApi(BaseApi):

    need_params = {
    }
    def post(self, request, params):
        data = rocket_ctl.sync_rockets(**params)
        return data
