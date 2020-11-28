from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest

from .base import AliyunCli


class AliyunECS(AliyunCli):
    '''
    阿里云ECS
    '''
    def get_ecses(self, instance_ids=[], page_num=1, page_size=20):
        request = DescribeInstancesRequest()
        request.set_accept_format('json')
        if instance_ids:
            request.set_InstanceIds(instance_ids)
        request.set_PageNumber(page_num)
        request.set_PageSize(page_size)

        data = self._request(request)
        total = data.get('TotalCount')
        data = data.get('Instances')
        data_list = data.get('Instance')
        data = {
            'total': total,
            'data_list': data_list,
        }
        return data
