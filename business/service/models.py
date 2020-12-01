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
    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE)
    environment = models.ForeignKey(EnvironmentModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'service_environment'


class ServiceAssetModel(BaseModel):
    '''
    服务关联资产模块
    '''
    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE)
    asset = models.ForeignKey(AssetModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'service_asset'
