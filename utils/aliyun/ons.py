from aliyunsdkons.request.v20190214.OnsInstanceInServiceListRequest import OnsInstanceInServiceListRequest
from aliyunsdkons.request.v20190214.OnsTopicListRequest import OnsTopicListRequest
from aliyunsdkons.request.v20190214.OnsGroupListRequest import OnsGroupListRequest
from aliyunsdkons.request.v20190214.OnsGroupSubDetailRequest import OnsGroupSubDetailRequest

from .base import AliyunCli


class AliyunONS(AliyunCli):
    '''
    阿里云消息队列
    '''
    def get_rockets(self):
        '''
        获取RocketMQ列表
        '''
        request = OnsInstanceInServiceListRequest()
        request.set_accept_format('json')

        data = self._request(request)
        data = data.get('Data')
        data_list = data.get('InstanceVO')
        data = {
            'total': len(data_list),
            'data_list': data_list,
        }
        return data

    def get_rocket_topics(self, instance_id):
        '''
        获取RocketMQ Topic
        '''
        request = OnsTopicListRequest()
        request.set_accept_format('json')
        request.set_InstanceId(instance_id)

        data = self._request(request)
        data = data.get('Data')
        data_list = data.get('PublishInfoDo')
        data = {
            'total': len(data_list),
            'data_list': data_list,
        }
        return data


    def get_rocket_groups(self, instance_id):
        '''
        获取RocketMQ Group
        '''
        request = OnsGroupListRequest()
        request.set_accept_format('json')
        request.set_InstanceId(instance_id)

        data = self._request(request)
        data = data.get('Data')
        data_list = data.get('SubscribeInfoDo')
        data = {
            'total': len(data_list),
            'data_list': data_list,
        }
        return data

    def get_rocket_group_topics(self, rocket_instance_id, group_id):
        '''
        获取RocketMQ Group订阅的Topic
        '''
        request = OnsGroupSubDetailRequest()
        request.set_accept_format('json')
        request.set_InstanceId(rocket_instance_id)
        request.set_GroupId(group_id)
        data = self._request(request)
        return data
