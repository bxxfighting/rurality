from django.db import models
from base.models import BaseModel


class FieldTemplateModel(BaseModel):
    '''
    字段模板
    '''
    model_name = '字段模板'
    model_sign = 'field_template'

    name = models.CharField('名称', max_length=128)
    sign = models.CharField('标识', max_length=128)
    rank = models.IntegerField('排序值')
    remark = models.TextField('备注', default='')

    class Meta:
        db_table = 'field_template'


class FormTemplateModel(BaseModel):
    '''
    表单模板
    '''
    model_name = '表单模板'
    model_sign = 'form_template'

    TYP_CUSTOM = 'custom'
    TYP_CHOICES = (
        (TYP_CUSTOM, '自定义模板'),
    )

    name = models.CharField('名称', max_length=128)
    typ = models.CharField('类型', max_length=128, choices=TYP_CHOICES)
    enabled = models.BooleanField('是否启用', default=False)
    remark = models.TextField('备注', default='')

    class Meta:
        db_table = 'form_template'


class FormFieldTemplateModel(BaseModel):
    '''
    表单字段模板
    '''
    model_name = '表单字段模板'
    model_sign = 'form_field_template'

    form = models.ForeignKey(FormTemplateModel, on_delete=models.CASCADE)
    field = models.ForeignKey(FormTemplateModel, on_delete=models.CASCADE)
    name = models.CharField('名称', max_length=128)
    sign = models.CharField('标识', max_length=128)
    rank = models.IntegerField('排序值')
    remark = models.TextField('备注', default='')

    class Meta:
        db_table = 'form_field_template'


class FlowTemplateModel(BaseModel):
    '''
    流程模板
    '''
    model_name = '流程模板'
    model_sign = 'flow_template'

    name = models.CharField('名称', max_length=128)
    sign = models.CharField('标识', max_length=128)

    class Meta:
        db_table = 'flow_template'


class FlowNodeTemplateModel(BaseModel):
    '''
    流程节点模板
    '''
    model_name = '流程节点模板'
    model_sign = 'flow_node_template'

    name = models.CharField('名称', max_length=128)
    sign = models.CharField('标识', max_length=128)

    class Meta:
        db_table = 'flow_node_template'
