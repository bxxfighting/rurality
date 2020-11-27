import logging
import ujson as json
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException

from base import errors


logger = logging.getLogger('error')


class AliyunCli:
    '''
    阿里云接口基础类
    '''

    def __init__(self, key, secret, region_id):
        self.access_key_id= key
        self.access_secret = secret
        self.region_id = region_id
        self.client = AcsClient(self.access_key_id, self.access_secret, self.region_id)

    def _request(self, request):
        '''
        基础请求方法，所有请求完全在这里完成
        增加异常处理，记录异常log并返回特定异常
        '''
        try:
            response = self.client.do_action_with_exception(request)
            data = json.loads(response)
            return data
        except Exception as e:
            logger.exception({'exception': e,'query': request.get_query_params()})
            raise errors.AliyunError

    def reset_region(self, region_id):
        self.region_id = region_id
        self.client = AcsClient(self.access_key_id, self.access_secret, self.region_id)
