from base.api import BaseApi
from asset.ecs.controllers import domain as domain_ctl


class ListEcsDomainApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('ECS ID', 'required int'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = domain_ctl.get_ecs_domains(**params)
        return data
