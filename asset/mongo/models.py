from django.db import models
from base.models import BaseModel


class MongoModel(BaseModel):
    '''
    Mongo实例
    '''
    model_name = 'Mongo'
    model_sign = 'mongo'

    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例id', max_length=128)
    typ = models.CharField('数据库类型', max_length=128)
    version = models.CharField('数据库版本', max_length=128)
    db_typ = models.CharField('复制集/分片', max_length=128)
    net_typ = models.CharField('EIP/VPC', max_length=128)
    replica_count = models.IntegerField('复制集节点数')
    region_id = models.CharField('地域', max_length=128)
    zone_id = models.CharField('可用区', max_length=128)
    connection = models.CharField('连接字符串', max_length=128)
    desc = models.TextField('描述', null=True)

    class Meta:
        db_table = 'mongo'


class MongoAccountModel(BaseModel):
    '''
    Mongo账号
    '''
    model_name = 'Mongo账号'
    model_sign = 'mongo_account'

    ST_AVAILABLE = 'Available'
    ST_UNAVAILABLE = 'Unavailable'
    ST_CHOICES = (
        (ST_AVAILABLE, '可用'),
        (ST_UNAVAILABLE, '不可用'),
    )

    TYP_MONGOS = 'mongos'
    TYP_SHARD = 'shard'
    TYP_CHOICES = (
        (TYP_MONGOS, 'mongos'),
        (TYP_SHARD, 'shard'),
    )

    mongo = models.ForeignKey(MongoModel, on_delete=models.CASCADE)
    username = models.CharField('用户名', max_length=128)
    password = models.CharField('密码', max_length=128)
    status = models.CharField('状态', max_length=128, choices=ST_CHOICES)
    typ = models.CharField('类型', max_length=128, choices=TYP_CHOICES)
    desc = models.TextField('备注', null=True)

    class Meta:
        db_table = 'mongo_account'
