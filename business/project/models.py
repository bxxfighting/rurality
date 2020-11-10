from django.db import models
from base.models import BaseModel
from account.models import UserModel


class ProjectModel(BaseModel):
    '''
    项目
    '''
    model_name = '项目'
    model_sign = 'project'

    name = models.CharField('名称', max_length=128)
    remark = models.TextField('备注', null=True)

    class Meta:
        db_table = 'project'


class ProjectUserModel(BaseModel):
    '''
    项目用户
    '''
    model_name = '项目用户'
    model_sign = 'project_user'

    TYP_MANAGER = 10
    TYP_MEMBER = 20
    TYP_CHOICES = (
        (TYP_MANAGER, '项目负责人'),
        (TYP_MEMBER, '普通成员'),
    )

    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    typ = models.SmallIntegerField('类型', choices=TYP_CHOICES)

    class Meta:
        db_table = 'project_user'
