from base.api import BaseApi
from asset.rds.controllers import database as database_ctl


class RdsDatabaseApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('Database ID', 'required int'),
    }
    def post(self, request, params):
        data = database_ctl.get_database(**params)
        return data


class ListRdsDatabaseApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'rds_id': ('RDS ID', 'optional int'),
        'rds_instance_id': ('RDS实例ID', 'optional str'),
        'keyword': ('关键字', 'optional str'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = database_ctl.get_databases(**params)
        return data


class ListRdsDatabaseAccountApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('Database ID', 'required int'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = database_ctl.get_database_accounts(**params)
        return data


class ListRdsDatabaseServiceApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('数据库ID', 'required int'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = database_ctl.get_database_services(**params)
        return data
