from django.db import models
from django.core.signing import TimestampSigner
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from base.models import BaseModel


class UserModel(BaseModel):
    '''
    用户表
    '''
    model_name = '用户'
    model_sign = 'user'

    TYP_NORMAL = 10
    TYP_LDAP = 20
    TYP_CHOICES = (
        (TYP_NORMAL, '标准用户'),
        (TYP_LDAP, 'LDAP用户'),
    )

    ST_NORMAL = 10
    ST_FORBIDDEN = 20
    ST_CHOICES = (
        (ST_NORMAL, '正常'),
        (ST_FORBIDDEN, '禁用'),
    )

    username = models.CharField('账户', max_length=128, db_index=True)
    password = models.CharField('密码', max_length=256, null=True, default=None)
    name = models.CharField('姓名', max_length=128, default='')
    email = models.CharField('邮箱', max_length=128, null=True, default='')
    phone = models.CharField('联系方式', max_length=64, null=True, default='')
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


class RoleModel(BaseModel):
    '''
    角色表
    '''
    model_name = '角色'
    model_sign = 'role'

    TYP_SYSTEM = 10
    TYP_NORMAL = 20
    TYP_CHOICES = (
        (TYP_SYSTEM, '系统角色'),
        (TYP_NORMAL, '普通角色'),
    )

    name = models.CharField('角色名', max_length=32)
    typ = models.IntegerField('类型', choices=TYP_CHOICES, default=TYP_NORMAL)
    sign = models.CharField('标识', max_length=32)

    class Meta:
        db_table = 'role'


class RoleUserModel(BaseModel):
    '''
    角色用户关系表
    '''
    model_name = '角色关联用户'
    model_sign = 'role_user'

    role = models.ForeignKey(RoleModel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'role_user'


class DepartmentModel(BaseModel):
    '''
    部门
    '''
    model_name = '部门'
    model_sign = 'department'

    name = models.CharField('名称', max_length=32)
    sign = models.CharField('标识', max_length=32)

    class Meta:
        db_table = 'department'


class DepartmentUserModel(BaseModel):
    '''
    部门与用户
    '''
    model_name = '部门关联用户'
    model_sign = 'department_user'

    TYP_MANAGER = 10
    TYP_MEMBER = 20
    TYP_CHOICES = (
        (TYP_MANAGER, '部门负责人'),
        (TYP_MEMBER, '普通成员'),
    )

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE)
    typ = models.SmallIntegerField('类型', choices=TYP_CHOICES, default=TYP_MEMBER)

    class Meta:
        db_table = 'department_user'


class ModModel(BaseModel):
    '''
    模块表
    '''
    model_name = '模块'
    model_sign = 'mod'

    name = models.CharField('模块名', max_length=32)
    sign = models.CharField('唯一标识', max_length=32)
    rank = models.IntegerField('排序')

    class Meta:
        db_table = 'mod'


class PermissionModel(BaseModel):
    '''
    权限
    '''
    model_name = '权限'
    model_sign = 'permission'

    TYP_OP = 10
    TYP_DATA = 20
    TYP_CHOICES = (
        (TYP_OP, '操作权限'),
        (TYP_DATA, '数据权限'),
    )

    mod = models.ForeignKey(ModModel, on_delete=models.CASCADE, null=True)
    name = models.CharField('权限名', max_length=128)
    typ = models.SmallIntegerField('类型', choices=TYP_CHOICES)
    sign = models.CharField('唯一标识', max_length=128, db_index=True)
    rank = models.IntegerField('排序')

    class Meta:
        db_table = 'permission'


class RoleModModel(BaseModel):
    '''
    角色模块
    '''
    model_name = '角色关联模块'
    model_sign = 'role_mod'

    role = models.ForeignKey(RoleModel, on_delete=models.CASCADE)
    mod = models.ForeignKey(ModModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'role_mod'


class RolePermissionModel(BaseModel):
    '''
    角色权限
    '''
    model_name = '角色关联权限'
    model_sign = 'role_permission'

    role = models.ForeignKey(RoleModel, on_delete=models.CASCADE)
    permission = models.ForeignKey(PermissionModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'role_permission'


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
