from django.db import models
from base.models import BaseModel


class EcsModel(BaseModel):
    '''
    ECS
    '''
    model_name = 'ECS'
    model_sign = 'ecs'

    CHARGE_TYP_PRE = 'PrePaid'
    CHARGE_TYP_POST = 'PostPaid'
    CHARGE_TYP_CHOICES = (
        (CHARGE_TYP_PRE, '包年包月'),
        (CHARGE_TYP_POST, '按量付费'),
    )

    region_id = models.CharField('地域ID', max_length=128)
    zone_id = models.CharField('可用区ID', max_length=128)
    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例ID', max_length=128)
    hostname = models.CharField('主机名', max_length=128)
    inner_ip = models.CharField('内网IP', max_length=128)
    outer_ip = models.CharField('外网IP', max_length=128)
    cpu = models.IntegerField('CPU')
    charge_typ = models.CharField('付费方式', max_length=128, choices=CHARGE_TYP_CHOICES)
    os = models.CharField('操作系统', max_length=128)
    memory = models.IntegerField('内存')
    dt_buy = models.DateTimeField('购买时间')

    class Meta:
        db_table = 'ecs'

    @property
    def web_url(self):
        host = 'https://ecs.console.aliyun.com'
        url = f'{host}/#/server/{self.instance_id}/detail?regionId={self.region_id}'
        return url

    def to_dict(self):
        data = super().to_dict()
        data['web_url'] = self.web_url
        return data
