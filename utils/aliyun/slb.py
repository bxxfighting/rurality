from aliyunsdkslb.request.v20140515.DescribeLoadBalancersRequest import DescribeLoadBalancersRequest
from aliyunsdkslb.request.v20140515.DescribeLoadBalancerAttributeRequest import DescribeLoadBalancerAttributeRequest
from aliyunsdkslb.request.v20140515.DescribeVServerGroupsRequest import DescribeVServerGroupsRequest
from aliyunsdkslb.request.v20140515.DescribeVServerGroupAttributeRequest import DescribeVServerGroupAttributeRequest

from .base import AliyunCli


class AliyunSLB(AliyunCli):
    '''
    阿里云SLB
    '''
    def get_slbs(self, page_num=1, page_size=20):
        '''
        '''
        request = DescribeLoadBalancersRequest()
        request.set_accept_format('json')
        request.set_PageNumber(page_num)
        request.set_PageSize(page_size)

        data = self._request(request)
        total = data.get('TotalCount')
        data = data.get('LoadBalancers')
        data_list = data.get('LoadBalancer')
        data = {
            'total': total,
            'data_list': data_list,
        }
        return data

    def get_slb_info(self, instance_id):
        '''
        获取SLB信息
        '''
        request = DescribeLoadBalancerAttributeRequest()
        request.set_accept_format('json')
        request.set_LoadBalancerId(instance_id)
        data = self._request(request)

        listen_data = data.get('ListenerPortsAndProtocol')
        listens = listen_data.get('ListenerPortAndProtocol')

        backend_server_data = data.get('BackendServers')
        backend_servers = backend_server_data.get('BackendServer')
        data = {
            'backend_servers': backend_servers,
            'listens': listens,
        }
        return data

    def get_vserver_groups(self, slb_instance_id):
        '''
        获取虚拟服务组
        '''
        request = DescribeVServerGroupsRequest()
        request.set_accept_format('json')
        request.set_LoadBalancerId(slb_instance_id)
        data = self._request(request)
        data= data.get('VServerGroups')
        data_list = data.get('VServerGroup')
        data = {
            'total': len(data_list),
            'data_list': data_list,
        }
        return data

    def get_vserver_group_backend_servers(self, instance_id):
        '''
        获取虚拟服务组后端服务器
        '''
        request = DescribeVServerGroupAttributeRequest()
        request.set_accept_format('json')
        request.set_VServerGroupId(instance_id)
        data = self._request(request)
        data = data.get('BackendServers')
        data_list = data.get('BackendServer')
        data = {
            'total': len(data_list),
            'data_list': data_list,
        }
        return data
