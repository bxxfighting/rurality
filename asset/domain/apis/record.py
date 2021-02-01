from base.api import BaseApi
from asset.domain.controllers import record as record_ctl


class CreateDomainRecordApi(BaseApi):

    need_params = {
        'domain_id': ('域名ID', 'required int'),
        'rr': ('RR', 'required str'),
        'typ': ('类型', 'required str'),
        'value': ('记录值', 'required str'),
    }
    def post(self, request, params):
        record_ctl.create_domain_record(**params)


class DeleteDomainRecordApi(BaseApi):

    need_params = {
        'obj_id': ('解析记录ID', 'required int'),
    }
    def post(self, request, params):
        record_ctl.delete_domain_record(**params)


class DomainRecordApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('解析记录ID', 'required int'),
    }
    def get(self, request, params):
        data = record_ctl.get_domain_record(**params)
        return data


class ListDomainRecordApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'domain_id': ('域名ID', 'optional int'),
        'keyword': ('关键词', 'optional str'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def get(self, request, params):
        data = record_ctl.get_domain_records(**params)
        return data


class ListDomainRecordServiceApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('解析记录ID', 'required int'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def get(self, request, params):
        data = record_ctl.get_domain_record_services(**params)
        return data
