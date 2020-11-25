from base.api import BaseApi
from asset.manager.controllers import aliyun_key as aliyun_key_ctl


class CreateAliyunKeyApi(BaseApi):

    need_params = {
        'key': ('阿里云key', 'required str 128'),
        'secret': ('阿里云密钥', 'required str 128'),
    }
    def post(self, request, params):
        data = aliyun_key_ctl.create_aliyun_key(**params)
        return data


class UpdateAliyunKeyApi(BaseApi):

    need_params = {
        'obj_id': ('阿里云key ID', 'required int'),
        'key': ('阿里云key', 'required str 128'),
        'secret': ('阿里云密钥', 'required str 128'),
    }
    def post(self, request, params):
        data = aliyun_key_ctl.update_aliyun_key(**params)
        return data


class DeleteAliyunKeyApi(BaseApi):

    need_params = {
        'obj_id': ('阿里云key ID', 'required int'),
    }
    def post(self, request, params):
        data = aliyun_key_ctl.delete_aliyun_key(**params)
        return data


class AliyunKeyApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('阿里云key ID', 'required int'),
    }
    def post(self, request, params):
        data = aliyun_key_ctl.get_aliyun_key(**params)
        return data


class ListAliyunKeyApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = aliyun_key_ctl.get_aliyun_keys(**params)
        return data


class SetAliyunKeyStatusApi(BaseApi):

    need_params = {
        'obj_id': ('阿里云key ID', 'required int'),
        'status': ('状态', 'required int'),
    }
    def post(self, request, params):
        data = aliyun_key_ctl.set_aliyun_key_status(**params)
        return data
