from aliyunsdkrds.request.v20140815.DescribeDBInstancesRequest import DescribeDBInstancesRequest
from aliyunsdkrds.request.v20140815.DescribeDatabasesRequest import DescribeDatabasesRequest
from aliyunsdkrds.request.v20140815.DescribeDBInstanceAttributeRequest import DescribeDBInstanceAttributeRequest
from aliyunsdkrds.request.v20140815.DescribeAccountsRequest import DescribeAccountsRequest
from aliyunsdkrds.request.v20140815.CreateDatabaseRequest import CreateDatabaseRequest
from aliyunsdkrds.request.v20140815.GrantAccountPrivilegeRequest import GrantAccountPrivilegeRequest

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

    def create_database(self, instance_id, name, charset='utf8mb4'):
        request = CreateDatabaseRequest()
        request.set_accept_format('json')
        request.set_DBInstanceId(instance_id)
        request.set_DBName(name)
        request.set_CharacterSetName(charset)
        data = self._request(request)
        return data

    def create_account(self, instance_id, username, password, remark='', typ='Normal'):
        request = CreateAccountRequest()
        request.set_accept_format('json')
        request.set_DBInstanceId(instance_id)
        request.set_AccountName(username)
        request.set_AccountPassword(password)
        request.set_AccountDescription(remark)
        request.set_AccountType(typ)
        data = self._request(request)
        return data

    def grant_account_privilege(self, instance_id, account_name, db_name, privilege):
        request = GrantAccountPrivilegeRequest()
        request.set_accept_format('json')
        request.set_DBInstanceId(instance_id)
        request.set_AccountName(account_name)
        request.set_DBName(db_name)
        request.set_AccountPrivilege(privilege)
        data = self._request(request)
        return data
