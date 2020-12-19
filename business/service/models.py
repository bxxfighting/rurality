from django.db import models
from base.models import BaseModel
from business.project.models import ProjectModel
from asset.manager.models import AssetModel
from account.models import DepartmentModel
from account.models import UserModel


class EnvironmentModel(BaseModel):
    '''
    环境
    qa/release/prod
    '''
    model_name = '环境'
    model_sign = 'environment'

    name = models.CharField('名称', max_length=128)
    sign = models.CharField('标识', max_length=128)
    rank = models.IntegerField('排序值', default=0)
    remark = models.TextField('备注', default='', null=True)

    class Meta:
        db_table = 'environment'


class ServiceModel(BaseModel):
    '''
    服务
    '''
    model_name = '服务'
    model_sign = 'service'

    name = models.CharField('名称', max_length=128)
    sign = models.CharField('标识', max_length=128)
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    remark = models.TextField('备注', null=True)

    class Meta:
        db_table = 'service'


class DepartmentServiceModel(BaseModel):
    '''
    部门关联服务
    '''
    model_name = '部门服务'
    model_sign = 'department_service'

    department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE)
    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'department_service'


class ServiceUserModel(BaseModel):
    '''
    服务用户
    '''
    model_name = '服务用户'
    model_sign = 'service_user'

    TYP_MANAGER = 10
    TYP_MEMBER = 20
    TYP_CHOICES = (
        (TYP_MANAGER, '服务负责人'),
        (TYP_MEMBER, '普通成员'),
    )

    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    typ = models.SmallIntegerField('类型', choices=TYP_CHOICES)

    class Meta:
        db_table = 'service_user'


class ServiceEnvironmentModel(BaseModel):
    '''
    服务环境
    不同服务可能并不一定有相同数量的环境
    如果是强制必须都有的，则可以不使用此关联表
    '''
    model_name = '服务环境'
    model_sign = 'service_environment'

    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE)
    environment = models.ForeignKey(EnvironmentModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'service_environment'


class ServiceAssetModel(BaseModel):
    '''
    服务关联资产模块
    '''
    model_name = '服务资产模块'
    model_sign = 'service_asset'

    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE)
    asset = models.ForeignKey(AssetModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'service_asset'


class ServiceAssetObjModel(BaseModel):
    '''
    服务关联资产实例
    '''
    model_name = '服务资产实例'
    model_sign = 'service_asset_obj'

    TYP_ECS = 'ecs'
    TYP_RDS = 'rds'
    TYP_SLB = 'slb'
    TYP_SLB_SERVER_GROUP = 'slb_server_group'
    TYP_DNS = 'dns'
    TYP_REDIS = 'redis'
    TYP_MONGO = 'mongo'
    TYP_ROCKET = 'rocket'
    TYP_KAFKA = 'kafka'

    TYP_CHOICES = (
        (TYP_ECS, 'ECS'),
        (TYP_RDS, 'RDS'),
        (TYP_SLB, 'SLB'),
        (TYP_SLB_SERVER_GROUP, 'SLB服务器组'),
        (TYP_DNS, 'DNS'),
        (TYP_REDIS, 'Redis'),
        (TYP_MONGO, 'Mongo'),
        (TYP_ROCKET, 'Rocket'),
        (TYP_KAFKA, 'Kafka'),
    )

    ST_PENDING_ADD = 10
    ST_SUCCESS_ADD = 20
    ST_FAILED_ADD = 30
    ST_PENDING_REMOVE = 40
    ST_SUCCESS_REMOVE = 50
    ST_FAILED_REMOVE = 60
    ST_CHOICES = (
        (ST_PENDING_ADD, '等待添加'),
        (ST_SUCCESS_ADD, '添加成功'),
        (ST_FAILED_ADD, '添加失败'),
        (ST_PENDING_REMOVE, '等待删除'),
        (ST_SUCCESS_REMOVE, '删除成功'),
        (ST_FAILED_REMOVE, '删除失败'),
    )

    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE, verbose_name='服务')
    environment = models.ForeignKey(EnvironmentModel, on_delete=models.CASCADE, verbose_name='环境')
    typ = models.CharField('资产类型', max_length=128, choices=TYP_CHOICES)
    status = models.SmallIntegerField('状态', choices=ST_CHOICES, default=ST_PENDING_ADD)
    asset_obj_id = models.IntegerField('资产实例ID', db_index=True)

    class Meta:
        db_table = 'service_asset_obj'
