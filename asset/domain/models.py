from django.db import models
from base.models import BaseModel


class DomainModel(BaseModel):
    '''
    域名
    '''
    model_name = '域名'
    model_sign = 'domain'

    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例id', max_length=128)
    record_count = models.IntegerField('解析记录数')

    class Meta:
        db_table = 'domain'

    @property
    def web_url(self):
        host = 'https://dns.console.aliyun.com'
        url = f'{host}/#/dns/setting/{self.name}'
        return url

    def to_dict(self):
        data = super().to_dict()
        data['web_url'] = self.web_url
        return data


class DomainRecordModel(BaseModel):
    '''
    域名解析记录
    '''
    model_name = '域名解析记录'
    model_sign = 'domain_record'

    domain = models.ForeignKey(DomainModel, on_delete=models.CASCADE, verbose_name='域名')
    fullname = models.CharField('完整域名', max_length=256)
    instance_id = models.CharField('实例id', max_length=128)
    name = models.CharField('主域名', max_length=128)
    value = models.CharField('value', max_length=128)
    typ = models.CharField('类型', max_length=128)
    rr = models.CharField('RR', max_length=128)
    enabled = models.BooleanField('是否启用', default=False)

    class Meta:
        db_table = 'domain_record'

    @property
    def web_url(self):
        host = 'https://dns.console.aliyun.com'
        url = f'{host}/#/dns/setting/{self.name}'
        return url

    def to_dict(self):
        data = super().to_dict()
        data['web_url'] = self.web_url
        return data


class DomainRecordAssetModel(BaseModel):
    '''
    域名解析关联资产实例
    '''
    model_name = '域名解析记录关联资产实例'
    model_sign = 'domain_record_asset'

    TYP_ECS = 'ecs'
    TYP_SLB = 'slb'
    TYP_CHOICES = (
        (TYP_ECS, 'ECS实例'),
        (TYP_SLB, 'SLB实例'),
    )

    record = models.ForeignKey(DomainRecordModel, on_delete=models.CASCADE, verbose_name='域名')
    asset_obj_id = models.IntegerField('资产实例ID', db_index=True)
    typ = models.CharField('类型', max_length=128, choices=TYP_CHOICES)

    class Meta:
        db_table = 'domain_record_asset'
