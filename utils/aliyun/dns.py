from aliyunsdkalidns.request.v20150109.DescribeDomainsRequest import DescribeDomainsRequest
from aliyunsdkalidns.request.v20150109.DescribeDomainRecordsRequest import DescribeDomainRecordsRequest
from aliyunsdkalidns.request.v20150109.DescribeDomainRecordInfoRequest import DescribeDomainRecordInfoRequest
from aliyunsdkalidns.request.v20150109.AddDomainRecordRequest import AddDomainRecordRequest
from aliyunsdkalidns.request.v20150109.DeleteDomainRecordRequest import DeleteDomainRecordRequest

from .base import AliyunCli


class AliyunDNS(AliyunCli):
    '''
    阿里云DNS
    '''
    def get_domains(self, page_num=1, page_size=20):
        '''
        获取域名
        '''
        request = DescribeDomainsRequest()
        request.set_accept_format('json')
        request.set_PageNumber(page_num)
        request.set_PageSize(page_size)

        data = self._request(request)
        total = data.get('TotalCount')
        data = data.get('Domains')
        data_list = data.get('Domain')
        data = {
            'total': total,
            'data_list': data_list,
        }
        return data

    def get_domain_records(self, domain_name, page_num=1, page_size=20):
        '''
        获取域名解析记录列表
        '''
        request = DescribeDomainRecordsRequest()
        request.set_accept_format('json')
        request.set_DomainName(domain_name)
        request.set_PageNumber(page_num)
        request.set_PageSize(page_size)

        data = self._request(request)
        total = data.get('TotalCount')
        data = data.get('DomainRecords')
        data_list = data.get('Record')
        data = {
            'total': total,
            'data_list': data_list,
        }
        return data

    def get_domain_record(self, instance_id):
        '''
        获取域名解析记录
        '''
        request = DescribeDomainRecordInfoRequest()
        request.set_accept_format('json')
        request.set_RecordId(instance_id)
        data = self._request(request)
        return data

    def create_domain_record(self, domain_name, rr, typ, value):
        '''
        添加域名解析记录
        '''
        request = AddDomainRecordRequest()
        request.set_accept_format('json')
        request.set_DomainName(domain_name)
        request.set_RR(rr)
        request.set_Type(typ)
        request.set_Value(value)
        data = self._request(request)
        record_id = data.get('RecordId')
        return record_id

    def delete_domain_record(self, instance_id):
        '''
        删除域名解析记录
        '''
        request = DeleteDomainRecordRequest()
        request.set_accept_format('json')
        request.set_RecordId(instance_id)
        data = self._request(request)
        record_id = data.get('RecordId')
        return record_id
