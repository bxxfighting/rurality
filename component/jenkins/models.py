from django.db import models
from base.models import BaseModel


class JenkinsServerModel(BaseModel):
    '''
    Jenkins服务实例
    不同公司jenkins的使用情况不同
    有的可能线上环境和测试环境使用不同的jenkins，有的可能使用同一个jenkins
    有的可能部署一台机器上，有的可能部署在k8s上
    不论是哪一种，我都统一采用相同的管理方式
    有几个jenkins就录入几个，然后服务不同环境可以关联不同的jenkins job
    当然了，如果公司就是使用同一个或者非常明确不同环境使用的jenkins
    可以对服务关联job的方式进行改造，使其更容易管理
    '''
    model_name = 'Jenkins服务'
    model_sign = 'jenkins_server'

    # 是否可以查看密码权限
    # 如果拥有编辑权限，则必须给查看密码权限
    PASSWORD_PERMISSION = 'jenkins-account-password'

    name = models.CharField('名称', max_length=128)
    host = models.CharField('访问地址', max_length=256)
    username = models.CharField('用户名', max_length=128)
    password = models.CharField('密码', max_length=128)
    # Jenkins登录后 -> 点击用户名 -> Configure -> API Token，输入名称生成token
    token = models.CharField('认证token', max_length=128)

    class Meta:
        db_table = 'jenkins_server'

    def to_dict(self, has_password=False):
        data = super().to_dict()
        if not has_password:
            data['password'] = '******'
            data['to_dict'] = '******'
        return data


class JenkinsJobModel(BaseModel):
    '''
    jenkins job
    '''
    model_name = 'Jenkins Job'
    model_sign = 'jenkins_job'

    server = models.ForeignKey(JenkinsServerModel, on_delete=models.CASCADE)
    name = models.CharField('名称', max_length=128)
    url = models.CharField('访问地址', max_length=256)

    class Meta:
        db_table = 'jenkins_job'


class JenkinsJobBuildModel(BaseModel):
    '''
    Jenkins Job构建信息
    有关queue_number: 在jenkins中触发job，都是先进入任务队列(不论是否有多个要执行)
    然后再通过调度开始执行，因此，在触发job时，得到的是一个队列号，
    之后，需要通过这个队列号获取构建后的构建号(其它功能都需要使用构建号)
    这个队列号在官方文档中说在job完成后，最多保留五分钟，因此要及时使用
    (five minutes after the job completes)
    '''

    ST_PENDING = 10
    ST_RUNNING = 20
    ST_SUCCESS = 30
    ST_FAILURE = 40
    ST_ABORTED = 50
    ST_CANCELLED = 60
    ST_CHOICES = (
        (ST_PENDING, '等待'),
        (ST_RUNNING, '执行中'),
        (ST_SUCCESS, '成功'),
        (ST_FAILURE, '失败'),
        (ST_ABORTED, '中止'),
        (ST_CANCELLED, '取消'),
    )
    # 代表结束的状态
    END_STATUS = (ST_SUCCESS, ST_FAILURE, ST_ABORTED, ST_CANCELLED,)

    server = models.ForeignKey(JenkinsServerModel, on_delete=models.CASCADE)
    job = models.ForeignKey(JenkinsJobModel, on_delete=models.CASCADE)
    status = models.IntegerField('状态', choices=ST_CHOICES)
    queue_number = models.IntegerField('队列ID')
    build_number= models.IntegerField('构建ID', null=True)
    build_url = models.TextField('构建地址', null=True)
    build_output = models.TextField('构建信息', null=True)

    class Meta:
        db_table = 'jenkins_job_build'
