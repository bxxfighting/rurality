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

    class Meta:
        db_table = 'field_template'


class FormTemplateModel(BaseModel):
    '''
    表单模板
    '''
    model_name = '表单模板'
    model_sign = 'form_template'

    name = models.CharField('名称', max_length=128)

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
