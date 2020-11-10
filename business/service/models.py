from django.db import models
from base.models import BaseModel
from business.project.models import ProjectModel
from account.models import DepartmentModel
from account.models import UserModel


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
