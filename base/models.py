from abc import abstractmethod

from datetime import datetime
from django.db import models
from django.forms.models import model_to_dict

from utils import time_utils


class BaseManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class BaseModel(models.Model):
    '''
    基础model类
    '''
    model_name = ''
    model_sign = ''

    dt_create = models.DateTimeField('创建时间', auto_now_add=True)
    dt_update = models.DateTimeField('更新时间', auto_now=True)
    is_deleted = models.BooleanField('是否删除', default=False)

    objects = BaseManager()
    src_objects = models.Manager()

    class Meta:
        abstract = True

    @classmethod
    def field_verbose_name(cls, field):
        '''
        字段中文名
        '''
        return cls._meta.get_field(field).verbose_name

    def to_dict(self):
        columns = self._meta.fields
        data = {}
        for column in columns:
            column_name = column.name
            column_typ = column.get_internal_type()
            # 所有使用choices的字段，返回当前值的描述
            if column.choices:
                method = 'get_{}_display'.format(column_name)
                data['{}_desc'.format(column_name)] = getattr(self, method)()
            value = getattr(self, column_name)
            # 统一格式化时间输出
            if column_typ == 'DateTimeField' and value:
                value = time_utils.datetime2str_by_format(value, '%Y-%m-%d %H:%M:%S')
            elif column_typ == 'ForeignKey' and value:
                value = value.id
                column_name = '{}_id'.format(column_name)
            data[column_name] = value
        data.pop('is_deleted')
        return data

    @classmethod
    def check_choices(cls, field_name, field_value):
        field = cls._meta.get_field(field_name)
        if field_value not in dict(field.choices).keys():
            return False
        return True
