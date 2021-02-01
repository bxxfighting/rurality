from django.db import models
from base.models import BaseModel


class LdapConfigModel(BaseModel):
    '''
    LDAP配置
    '''
    model_name = 'LDAP服务配置'
    model_sign = 'ldap_config'

    # 是否可以查看密码权限
    # 如果拥有编辑权限，则必须给查看密码权限
    PASSWORD_PERMISSION = 'ldap-account-password'

    # 类似这样格式：ldap://ldap.oldb.top:389
    host = models.CharField('地址', max_length=128)
    # ldap管理员账号DN：类似这样cn=admin,dc=oldb,dc=top
    admin_dn = models.CharField('管理员DN', max_length=128)
    admin_password = models.CharField('管理员密码', max_length=128)
    # 所有用户在此节点下
    member_base_dn = models.CharField('用户基础DN', max_length=128)

    class Meta:
        db_table = 'ldap_config'

    @classmethod
    def none_to_dict(cls):
        '''
        不存在时，返回内容
        '''
        data = {
            'host': '',
            'admin_dn': '',
            'admin_password': '',
            'member_base_dn': '',
        }
        return data

    def to_dict(self, has_password=False):
        data = super().to_dict()
        if not has_password:
            data['admin_password'] = '******'
        return data
