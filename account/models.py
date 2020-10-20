from django.db import models
from django.core.signing import TimestampSigner
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from base.models import BaseModel


class UserModel(BaseModel):
    '''
    用户表
    '''
    TYP_NORMAL = 10
    TYP_LDAP = 20
    ST_CHOICES = (
        (TYP_NORMAL, '标准用户'),
        (TYP_LDAP, 'LDAP用户'),
    )

    ST_NORMAL = 1
    ST_FORBIDDEN = 2
    ST_CHOICES = (
        (ST_NORMAL, '正常'),
        (ST_FORBIDDEN, '禁用'),
    )

    username = models.CharField('账户', max_length=128)
    password = models.CharField('密码', max_length=256)
    name = models.CharField('姓名', max_length=128, default='')
    email = models.CharField('邮箱', max_length=128, default='')
    phone = models.CharField('联系方式', max_length=64, default='')
    status = models.IntegerField('状态', choices=ST_CHOICES, default=ST_NORMAL)
    typ = models.SmallIntegerField('类型', choices=TYP_CHOICES, default=TYP_NORMAL)

    class Meta:
        db_table = 'user'

    def to_dict(self):
        '''
        用户信息，不返回密码
        '''
        data = super().to_dict()
        data.pop('password')
        return data

    def set_password(self, password):
        '''
        设置密码
        '''
        self.password = make_password(password)
        self.save()

    def check_password(self, password):
        '''
        校验密码
        '''
        return check_password(password, self.password)

    def gen_token(self):
        '''
        生成接口认证的token
        '''
        signer = TimestampSigner()
        token = signer.sign(self.id)
        return token
