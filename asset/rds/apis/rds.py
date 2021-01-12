from base.api import BaseApi
from asset.rds.controllers import rds as rds_ctl


class RdsApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('RDS ID', 'required int'),
    }
    def post(self, request, params):
        data = rds_ctl.get_rds(**params)
        return data


class ListRdsApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'keyword': ('关键字', 'optional str'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = rds_ctl.get_rdses(**params)
        return data


class SyncRdsApi(BaseApi):

    need_params = {
    }
    def post(self, request, params):
        data = rds_ctl.sync_rdses(**params)
        return data
