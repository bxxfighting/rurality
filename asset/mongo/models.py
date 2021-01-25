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
    remark = models.TextField('备注', null=True)

    class Meta:
        db_table = 'mongo'

    @property
    def web_url(self):
        host = 'https://mongodb.console.aliyun.com'
        url = f'{host}/replicate/{self.region_id}/instances/{self.instance_id}/basicInfo'
        return url

    def to_dict(self):
        data = super().to_dict()
        data['web_url'] = self.web_url
        return data


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

    # 是否可以查看数据库密码权限
    # 如果拥有编辑权限，则必须给查看密码权限
    PASSWORD_PERMISSION = 'mongo-account-password'

    mongo = models.ForeignKey(MongoModel, on_delete=models.CASCADE)
    username = models.CharField('用户名', max_length=128)
    password = models.CharField('密码', max_length=128)
    status = models.CharField('状态', max_length=128, choices=ST_CHOICES)
    typ = models.CharField('类型', max_length=128, choices=TYP_CHOICES)
    remark = models.TextField('备注', null=True)

    class Meta:
        db_table = 'mongo_account'

    def to_dict(self, has_password=False):
        data = super().to_dict()
        if not has_password:
            data['password'] = '******'
        return data
