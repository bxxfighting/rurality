from base.api import BaseApi
from asset.slb.controllers import slb as slb_ctl


class SlbApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('SLB ID', 'required int'),
    }
    def post(self, request, params):
        data = slb_ctl.get_slb(**params)
        return data


class ListSlbApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'keyword': ('关键字', 'optional str'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = slb_ctl.get_slbs(**params)
        return data


class SyncSlbApi(BaseApi):

    need_params = {
    }
    def post(self, request, params):
        data = slb_ctl.sync_slbs(**params)
        return data
