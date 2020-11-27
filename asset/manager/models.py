from django.db import models
from base.models import BaseModel


class AliyunKeyModel(BaseModel):
    '''
    访问阿里云的key
    此key需要拥有所有权限，或者赋予此系统需要用的全部权限
    此key可以定期更新，以防key泄露
    '''
    model_name = '阿里云Key'
    model_sign = 'aliyun_key'

    ST_ENABLE = 10
    ST_DISABLE = 20
    ST_CHOICES = (
        (ST_ENABLE, '启用'),
        (ST_DISABLE, '禁用'),
    )

    key = models.CharField('key', max_length=128)
    secret = models.CharField('secret', max_length=128)
    status = models.SmallIntegerField('状态', choices=ST_CHOICES, default=ST_DISABLE)

    class Meta:
        db_table = 'aliyun_key'


class AssetModel(BaseModel):
    '''
    资产模块
    '''
    model_name = '资产模块'
    model_sign = 'asset'

    name = models.CharField('名称', max_length=128)
    sign = models.CharField('标识', max_length=128)
    rank = models.IntegerField('排序值')
    remark = models.TextField('备注')

    class Meta:
        db_table = 'asset'


class RegionModel(BaseModel):
    '''
    地域
    '''
    model_name = '地域'
    model_sign = 'region'

    ST_ENABLE = 10
    ST_DISABLE = 20
    ST_CHOICES = (
        (ST_ENABLE, '启用'),
        (ST_DISABLE, '禁用'),
    )

    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例ID', max_length=128)
    endpoint = models.CharField('接入点', max_length=128)
    status = models.SmallIntegerField('状态', choices=ST_CHOICES, default=ST_DISABLE)

    class Meta:
        db_table = 'region'


class ZoneModel(BaseModel):
    '''
    可用区
    '''
    model_name = '可用区'
    model_sign = 'zone'

    region = models.ForeignKey(RegionModel, on_delete=models.CASCADE, verbose_name='地域')
    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例ID', max_length=128)

    class Meta:
        db_table = 'zone'
