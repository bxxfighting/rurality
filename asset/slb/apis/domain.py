from base.api import BaseApi
from asset.slb.controllers import domain as domain_ctl


class ListSlbDomainApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('SLB ID', 'required int'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = domain_ctl.get_slb_domains(**params)
        return data
