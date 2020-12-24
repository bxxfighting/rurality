from aliyunsdkdds.request.v20151201.DescribeDBInstancesRequest import DescribeDBInstancesRequest
from aliyunsdkdds.request.v20151201.DescribeDBInstanceAttributeRequest import DescribeDBInstanceAttributeRequest
from aliyunsdkdds.request.v20151201.DescribeAccountsRequest import DescribeAccountsRequest

from .base import AliyunCli


class AliyunMongo(AliyunCli):
    '''
    阿里云Mongo
    '''
    def get_mongos(self, page_num=1, page_size=30):
        '''
        获取Mongo列表
        '''
        request = DescribeDBInstancesRequest()
        request.set_accept_format('json')
        request.set_PageNumber(page_num)
        request.set_PageSize(page_size)

        data = self._request(request)
        total = data.get('TotalCount')
        data = data.get('DBInstances')
        data_list = data.get('DBInstance')

        data = {
            'total': total,
            'data_list': data_list,
        }
        return data

    def get_mongo_attribute(self, instance_id):
        '''
        获取Mongo属性
        '''
        request = DescribeDBInstanceAttributeRequest()
        request.set_accept_format('json')
        request.set_DBInstanceId(instance_id)

        data = self._request(request)
        data = data.get('DBInstances')
        data = data.get('DBInstance')
        if data:
            data = data[0]
        return data

    def get_mongo_accounts(self, instance_id):
        '''
        获取Mongo账号
        '''
        request = DescribeAccountsRequest()
        request.set_accept_format('json')
        request.set_DBInstanceId(instance_id)
        data = self._request(request)
        data = data.get('Accounts')
        data_list = data.get('Account')
        data = {
            'total': len(data_list),
            'data_list': data_list,
        }
        return data
