from base.api import BaseApi
from business.service.controllers import asset as asset_ctl


class CreateServiceAssetApi(BaseApi):

    need_params = {
        'obj_id': ('服务ID', 'required int'),
        'asset_id': ('资产模块ID', 'required int'),
    }
    def post(self, request, params):
        data = asset_ctl.create_service_asset(**params)
        return data


class DeleteServiceAssetApi(BaseApi):

    need_params = {
        'obj_id': ('服务ID', 'required int'),
        'asset_id': ('资产模块ID', 'required int'),
    }
    def post(self, request, params):
        data = asset_ctl.delete_service_asset(**params)
        return data


class ListServiceAssetApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('服务ID', 'required int'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = asset_ctl.get_service_assets(**params)
        return data
