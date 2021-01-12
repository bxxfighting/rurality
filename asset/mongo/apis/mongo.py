from base.api import BaseApi
from asset.mongo.controllers import mongo as mongo_ctl


class MongoApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('Mongo ID', 'required int'),
    }
    def post(self, request, params):
        data = mongo_ctl.get_mongo(**params)
        return data


class ListMongoApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'keyword': ('关键字', 'optional str'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = mongo_ctl.get_mongos(**params)
        return data


class ListMongoServiceApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('Mongo ID', 'required int'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = mongo_ctl.get_mongo_services(**params)
        return data


class SyncMongoApi(BaseApi):

    need_params = {
    }
    def post(self, request, params):
        data = mongo_ctl.sync_mongos(**params)
        return data
