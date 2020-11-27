from aliyunsdkecs.request.v20140526.DescribeRegionsRequest import DescribeRegionsRequest
from aliyunsdkecs.request.v20140526.DescribeZonesRequest import DescribeZonesRequest

from .base import AliyunCli


class AliyunManager(AliyunCli):
    '''
    阿里云杂烩
    这里主要是一些没有归类的方法
    '''
    def get_regions(self):
        request = DescribeRegionsRequest()
        request.set_accept_format('json')
        data = self._request(request)
        data = data.get('Regions')
        data_list = data.get('Region')
        data = {
            'total': len(data_list),
            'data_list': data_list,
        }
        return data

    def get_zones(self, region_id):
        self.reset_region(region_id)
        request = DescribeZonesRequest()
        request.set_accept_format('json')
        data = self._request(request)
        data = data.get('Zones')
        data_list = data.get('Zone')
        data = {
            'total': len(data_list),
            'data_list': data_list,
        }
        return data
