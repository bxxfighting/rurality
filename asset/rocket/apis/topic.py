from base.api import BaseApi
from asset.rocket.controllers import topic as topic_ctl


class RocketTopicApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'obj_id': ('Topic ID', 'required int'),
    }
    def post(self, request, params):
        data = topic_ctl.get_topic(**params)
        return data


class ListRocketTopicApi(BaseApi):
    NEED_PERMISSION = False

    need_params = {
        'rocket_id': ('Rocket ID', 'optional int'),
        'rocket_instance_id': ('Rocket实例ID', 'optional str'),
        'keyword': ('关键词', 'optional str'),
        'page_num': ('页码', 'optional int'),
        'page_size': ('页容量', 'optional int'),
    }
    def post(self, request, params):
        data = topic_ctl.get_topics(**params)
        return data
