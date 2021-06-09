from aliyunsdkvpc.request.v20160428.DescribeVpcsRequest import DescribeVpcsRequest
from aliyunsdkvpc.request.v20160428.DescribeVSwitchAttributesRequest import DescribeVSwitchAttributesRequest
from aliyunsdkvpc.request.v20160428.DescribeVSwitchesRequest import DescribeVSwitchesRequest

from .base import AliyunCli


class AliyunVPC(AliyunCli):
    '''
    阿里云VPC
    '''
    def get_vpcs(self, page_num=1, page_size=20):
        '''
        获取VPC列表
        '''
        request = DescribeVpcsRequest()
        request.set_accept_format('json')
        request.set_PageNumber(page_num)
        request.set_PageSize(page_size)

        data = self._request(request)
        total = data.get('TotalCount')
        data = data.get('Vpcs')
        data_list = data.get('Vpc')

        data = {
            'total': total,
            'data_list': data_list,
        }
        return data

    def get_vswitches(self, vpc_instance_id, page_num=1, page_size=20):
        '''
        获取交换机列表
        '''
        request = DescribeVSwitchesRequest()
        request.set_accept_format('json')
        request.set_VpcId(vpc_instance_id)
        request.set_PageNumber(page_num)
        request.set_PageSize(page_size)

        data = self._request(request)
        total = data.get('TotalCount')
        data = data.get('VSwitches')
        data_list = data.get('VSwitch')

        data = {
            'total': total,
            'data_list': data_list,
        }
        return data

    def get_vswitch_attribute(self, instance_id):
        '''
        获取交换机属性
        '''
        request = DescribeVSwitchAttributesRequest()
        request.set_accept_format('json')
        request.set_VSwitchId(instance_id)
        data = self._request(request)
        return data
