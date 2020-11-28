from base.api import BaseApi
from asset.ecs.controllers import ecs as ecs_ctl


class EcsApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('ECS ID', 'required int'),
    }
    def post(self, request, params):
        data = ecs_ctl.get_ecs(**params)
        return data


class ListEcsApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = ecs_ctl.get_ecses(**params)
        return data
