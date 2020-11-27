from base.api import BaseApi
from asset.manager.controllers import region as region_ctl


class RegionApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('地域ID', 'required int'),
    }
    def post(self, request, params):
        data = region_ctl.get_region(**params)
        return data


class ListRegionApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'status': ('状态', 'optional int'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = region_ctl.get_regions(**params)
        return data


class SetRegionStatusApi(BaseApi):

    need_params = {
        'obj_id': ('地域ID', 'required int'),
        'status': ('状态', 'required int'),
    }
    def post(self, request, params):
        data = region_ctl.set_region_status(**params)
        return data


class ZoneApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('可用区ID', 'required int'),
    }
    def post(self, request, params):
        data = region_ctl.get_zone(**params)
        return data


class ListZoneApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'region_id': ('地域ID', 'required int'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = region_ctl.get_zones(**params)
        return data
