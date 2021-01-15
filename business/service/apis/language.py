from base.api import BaseApi
from business.service.controllers import language as language_ctl


class CreateLanguageApi(BaseApi):

    need_params = {
        'name': ('名称', 'required str 128'),
        'sign': ('标识', 'required str 128'),
    }
    def post(self, request, params):
        data = language_ctl.create_language(**params)
        return data


class UpdateLanguageApi(BaseApi):

    need_params = {
        'obj_id': ('编程语言ID', 'required int'),
        'name': ('名称', 'required str 128'),
        'sign': ('标识', 'required str 128'),
    }
    def post(self, request, params):
        data = language_ctl.update_language(**params)
        return data


class DeleteLanguageApi(BaseApi):

    need_params = {
        'obj_id': ('编程语言ID', 'required int'),
    }
    def post(self, request, params):
        data = language_ctl.delete_language(**params)
        return data


class ListLanguageApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = language_ctl.get_languages(**params)
        return data


class LanguageApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('编程语言ID', 'required int'),
    }

    def post(self, request, params):
        data = language_ctl.get_language(**params)
        return data
