from django.db import models
from base.models import BaseModel


class EcsModel(BaseModel):
    '''
    ECS
    '''
    model_name = 'ECS'
    model_sign = 'ecs'

    region_id = models.CharField('地域ID', max_length=128)
    zone_id = models.CharField('可用区ID', max_length=128)
    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例ID', max_length=128)
    hostname = models.CharField('主机名', max_length=128)
    inner_ip = models.CharField('内网IP', max_length=128)
    outer_ip = models.CharField('外网IP', max_length=128)
    cpu = models.IntegerField('CPU')
    os = models.CharField('操作系统', max_length=128)
    memory = models.IntegerField('内存')
    dt_buy = models.DateTimeField('购买时间')

    class Meta:
        db_table = 'ecs'
