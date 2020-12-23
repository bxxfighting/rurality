from django.db import models
from base.models import BaseModel


class RedisModel(BaseModel):
    '''
    Redis
    '''
    model_name = 'Redis'
    model_sign = 'redis'

    DEPLOY_TYP_CLUSTER = 'cluster'
    DEPLOY_TYP_STANDARD = 'standard'
    DEPLOY_TYP_SPLIT_RW= 'rwsplit'
    DEPLOY_TYP_NULL = 'NULL'
    DEPLOY_TYP_CHOICES = (
        (DEPLOY_TYP_CLUSTER, '集群版'),
        (DEPLOY_TYP_STANDARD, '标准版'),
        (DEPLOY_TYP_SPLIT_RW, '读写分离版'),
        (DEPLOY_TYP_NULL, '默认'),
    )

    name = models.CharField('名称', max_length=128)
    instance_id = models.CharField('实例id', max_length=128)
    version = models.CharField('版本', max_length=128)
    port = models.IntegerField('端口号')
    inner_ip = models.CharField('内网IP', max_length=128)
    deploy_typ = models.CharField('部署类型', max_length=128, choices=DEPLOY_TYP_CHOICES)
    username = models.CharField('用户名', max_length=128)
    region_id = models.CharField('区域', max_length=128)
    zone_id = models.CharField('可用区', max_length=128)
    connection = models.CharField('连接字符串', max_length=128)

    class Meta:
        db_table = 'redis'


class RedisAccountModel(BaseModel):
    '''
    Redis账号
    '''
    model_name = 'Redis账号'
    model_sign = 'redis_account'

    ST_AVAILABLE = 'Available'
    ST_UNAVAILABLE = 'Unavailable'
    ST_CHOICES = (
        (ST_AVAILABLE, '可用'),
        (ST_UNAVAILABLE, '不可用'),
    )

    TYP_NORMAL = 'Normal'
    TYP_SUPER = 'Super'
    TYP_CHOICES = (
        (TYP_NORMAL, '普通账号'),
        (TYP_SUPER, '超级账号'),
    )
    PRIVILEGE_ROLE_READ_ONLY = 'RoleReadOnly'
    PRIVILEGE_ROLE_READ_WRITE = 'RoleReadWrite'
    PRIVILEGE_ROLE_REPL = 'RoleRepl'
    PRIVILEGE_CHOICES = (
        (PRIVILEGE_ROLE_READ_ONLY, '只读'),
        (PRIVILEGE_ROLE_READ_WRITE, '读写'),
        (PRIVILEGE_ROLE_REPL, '复制'),
    )

    redis = models.ForeignKey(RedisModel, on_delete=models.CASCADE)
    username = models.CharField('用户名', max_length=128)
    password = models.CharField('密码', max_length=128)
    typ = models.CharField('类型', max_length=128, choices=TYP_CHOICES)
    status = models.CharField('状态', max_length=128, choices=ST_CHOICES)
    privilege = models.CharField('权限', max_length=128, choices=PRIVILEGE_CHOICES)

    class Meta:
        db_table = 'redis_account'
