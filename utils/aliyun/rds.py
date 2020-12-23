from aliyunsdkrds.request.v20140815.DescribeDBInstancesRequest import DescribeDBInstancesRequest
from aliyunsdkrds.request.v20140815.DescribeDatabasesRequest import DescribeDatabasesRequest
from aliyunsdkrds.request.v20140815.DescribeDBInstanceAttributeRequest import DescribeDBInstanceAttributeRequest
from aliyunsdkrds.request.v20140815.DescribeAccountsRequest import DescribeAccountsRequest

from .base import AliyunCli


class AliyunRDS(AliyunCli):
    '''
    阿里云RDS
    '''
    def get_rdses(self, page_num=1, page_size=20):
        request = DescribeDBInstancesRequest()
        request.set_accept_format('json')
        request.set_PageNumber(page_num)
        request.set_PageSize(page_size)

        data = self._request(request)
        total = data.get('TotalRecordCount')
        data = data.get('Items')
        data_list = data.get('DBInstance')
        data = {
            'total': total,
            'data_list': data_list,
        }
        return data

    def get_rds_accounts(self, instance_id, username=None, page_num=1, page_size=20):
        '''
        获取RDS下账号
        '''
        request = DescribeAccountsRequest()
        request.set_accept_format('json')
        request.set_PageNumber(page_num)
        request.set_PageSize(page_size)
        if username:
            request.set_AccountName(username)
        request.set_DBInstanceId(instance_id)
        data = self._request(request)
        data = data.get('Accounts')
        data_list = data.get('DBInstanceAccount')
        data = {
            'data_list': data_list,
        }
        return data

    def get_rds_databases(self, instance_id, page_num=1, page_size=20):
        request = DescribeDatabasesRequest()
        request.set_accept_format('json')
        request.set_DBInstanceId(instance_id)
        request.set_PageNumber(page_num)
        request.set_PageSize(page_size)

        data = self._request(request)
        data = data.get('Databases')
        data_list = data.get('Database')

        data = {
            'data_list': data_list,
        }
        return data

    def get_rds_attribute(self, instance_id):
        request = DescribeDBInstanceAttributeRequest()
        request.set_accept_format('json')
        request.set_DBInstanceId(instance_id)
        data = self._request(request)
        data = data.get('Items')
        data = data.get('DBInstanceAttribute')
        if data:
            data = data[0]
        return data
