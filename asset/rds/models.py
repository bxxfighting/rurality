from django.db import models
from base.models import BaseModel


class RdsModel(BaseModel):
    '''
    数据库实例
    '''
    model_name = 'RDS'
    model_sign = 'rds'

    DB_NET_TYP_INTERNET = 'Internet'
    DB_NET_TYP_INTRANET = 'Intranet'
    DB_NET_TYP_CHOICES = (
        (DB_NET_TYP_INTERNET, '外网'),
        (DB_NET_TYP_INTRANET, '内网'),
    )

    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例id', max_length=128)
    typ = models.CharField('数据库类型', max_length=128)
    version = models.CharField('数据库版本', max_length=128)
    db_typ = models.CharField('主从类型', max_length=128)
    region_id = models.CharField('地域', max_length=128)
    zone_id = models.CharField('可用区', max_length=128)
    db_net_typ = models.CharField('内网/外网', max_length=128, choices=DB_NET_TYP_CHOICES)
    net_typ = models.CharField('EIP/VPC', max_length=128)
    connection = models.CharField('连接字符串', max_length=128)
    desc = models.TextField('备注', default='', null=True)

    class Meta:
        db_table = 'rds'


class RdsAccountModel(BaseModel):
    '''
    数据库账号
    '''
    model_name = 'RDS账号'
    model_sign = 'rds_account'

    rds = models.ForeignKey(RdsModel, on_delete=models.CASCADE)
    username = models.CharField('用户名', max_length=128)
    password = models.CharField('密码', max_length=128)

    class Meta:
        db_table = 'rds_account'


class RdsDatabaseModel(BaseModel):
    '''
    数据库实例下的库
    '''
    model_name = '数据库实例'
    model_sign = 'rds_database'

    rds = models.ForeignKey(RdsModel, on_delete=models.CASCADE)
    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例ID', max_length=128)
    desc = models.TextField('描述')
    accounts = models.TextField('账号相关信息', default='', null=True)

    class Meta:
        db_table = 'rds_database'


class RdsDatabaseAccountModel(BaseModel):
    '''
    数据库实例账号
    '''
    model_name = '数据库实例账号'
    model_sign = 'rds_database_account'

    database = models.ForeignKey(RdsDatabaseModel, on_delete=models.CASCADE)
    account = models.ForeignKey(RdsAccountModel, on_delete=models.CASCADE)
    privilege = models.CharField('权限', max_length=128)

    class Meta:
        db_table = 'rds_database_account'
