from django.db import models
from base.models import BaseModel


class VpcModel(BaseModel):
    '''
    VPC
    '''
    model_name = 'VPC'
    model_sign = 'vpc'

    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例id', max_length=128)
    desc = models.TextField('描述')
    is_default = models.BooleanField('是否默认')
    cidr_block= models.CharField('网段', max_length=128)
    region_id = models.CharField('地区', max_length=128)
    vswitch_count = models.IntegerField('交换机数量')

    class Meta:
        db_table = 'vpc'


class VSwitchModel(BaseModel):
    '''
    VSwitch交换机
    '''
    model_name = '交换机'
    model_sign = 'vswitch'

    vpc = models.ForeignKey(VpcModel, on_delete=models.CASCADE)
    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例id', max_length=128)
    is_default = models.BooleanField('是否默认')
    desc = models.TextField('描述')
    cidr_block= models.CharField('网段', max_length=128)
    region_id = models.CharField('区域', max_length=128)
    zone_id = models.CharField('可用区', max_length=128)
    ip_count = models.IntegerField('可用IP数')

    class Meta:
        db_table = 'vswitch'
