from django.db import models
from base.models import BaseModel
from business.project.models import ProjectModel
from asset.manager.models import AssetModel
from account.models import DepartmentModel
from account.models import UserModel
from component.gitlab.models import GitlabProjectModel


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


class LanguageModel(BaseModel):
    '''
    编程语言
    '''
    model_name = '编程语言'
    model_sign = 'language'

    name = models.CharField('名称', max_length=128)
    sign = models.CharField('标识', max_length=128)

    class Meta:
        db_table = 'language'


class FrameModel(BaseModel):
    '''
    框架
    '''
    model_name = '框架'
    model_sign = 'frame'

    language = models.ForeignKey(LanguageModel, on_delete=models.CASCADE)
    name = models.CharField('名称', max_length=128)
    sign = models.CharField('标识', max_length=128)

    class Meta:
        db_table = 'frame'


class ServiceModel(BaseModel):
    '''
    服务
    '''
    model_name = '服务'
    model_sign = 'service'

    name = models.CharField('名称', max_length=128)
    sign = models.CharField('标识', max_length=128)
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, verbose_name='项目')
    language = models.ForeignKey(LanguageModel, on_delete=models.CASCADE, verbose_name='编程语言', null=True)
    frame = models.ForeignKey(FrameModel, on_delete=models.CASCADE, verbose_name='框架', null=True)
    gitlab = models.ForeignKey(GitlabProjectModel, on_delete=models.CASCADE, verbose_name='框架', null=True)
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
    model_name = '服务环境'
    model_sign = 'service_environment'

    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE)
    environment = models.ForeignKey(EnvironmentModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'service_environment'


class ServiceAssetModel(BaseModel):
    '''
    服务关联资产模块
    '''
    model_name = '服务资产模块'
    model_sign = 'service_asset'

    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE)
    asset = models.ForeignKey(AssetModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'service_asset'


class ServiceAssetObjModel(BaseModel):
    '''
    服务关联资产实例
    '''
    model_name = '服务资产实例'
    model_sign = 'service_asset_obj'

    TYP_ECS = 'ecs'
    TYP_RDS = 'rds'
    TYP_DATABASE = 'database'
    TYP_SLB = 'slb'
    TYP_SLB_SERVER_GROUP = 'slb_server_group'
    TYP_DNS = 'dns'
    TYP_REDIS = 'redis'
    TYP_MONGO = 'mongo'
    TYP_ROCKET_TOPIC = 'rocket_topic'
    TYP_KAFKA = 'kafka'
    TYP_DOMAIN = 'domain'

    TYP_CHOICES = (
        (TYP_ECS, 'ECS'),
        (TYP_RDS, 'RDS'),
        (TYP_DATABASE, '数据库'),
        (TYP_SLB, 'SLB'),
        (TYP_SLB_SERVER_GROUP, 'SLB服务器组'),
        (TYP_DNS, 'DNS'),
        (TYP_REDIS, 'Redis'),
        (TYP_MONGO, 'Mongo'),
        (TYP_ROCKET_TOPIC, 'Rocket Topic'),
        (TYP_KAFKA, 'Kafka'),
        (TYP_DOMAIN, '域名'),
    )

    ST_PENDING_ADD = 10
    ST_SUCCESS_ADD = 20
    ST_FAILED_ADD = 30
    ST_PENDING_REMOVE = 40
    ST_SUCCESS_REMOVE = 50
    ST_FAILED_REMOVE = 60
    ST_CHOICES = (
        (ST_PENDING_ADD, '等待添加'),
        (ST_SUCCESS_ADD, '添加成功'),
        (ST_FAILED_ADD, '添加失败'),
        (ST_PENDING_REMOVE, '等待删除'),
        (ST_SUCCESS_REMOVE, '删除成功'),
        (ST_FAILED_REMOVE, '删除失败'),
    )

    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE, verbose_name='服务')
    environment = models.ForeignKey(EnvironmentModel, on_delete=models.CASCADE, verbose_name='环境')
    typ = models.CharField('资产类型', max_length=128, choices=TYP_CHOICES)
    status = models.SmallIntegerField('状态', choices=ST_CHOICES, default=ST_PENDING_ADD)
    asset_obj_id = models.IntegerField('资产实例ID', db_index=True)

    class Meta:
        db_table = 'service_asset_obj'


class ServiceConfigModel(BaseModel):
    '''
    服务配置
    '''
    model_name = '服务配置'
    model_sign = 'service_config'

    # 无解析：不需要添加域名解析
    DNS_TYP_NONE = 'none'
    # 解析至ECS：原则是不推荐域名直接解析到ECS的，
    # 因为这样没办法配置负载均衡和高可用，当然测试环境这么弄是可以的
    DNS_TYP_ECS = 'ecs'
    # 解析至SLB：正常情况下所有域名都应该解析至SLB上，同时配置虚拟服务器组
    # 当前了，还是看实际使用，以后的其它操作都取决于这个决定
    # 比如，如果所有都统一使用虚拟服务器组，那么就只用写一套管理流程
    # 扩容、缩容、服务部署时上下流量等
    DNS_TYP_SLB = 'slb'
    DNS_TYP_CHOICES = (
        (DNS_TYP_NONE, '无解析'),
        (DNS_TYP_ECS, '解析至ECS'),
        (DNS_TYP_SLB, '解析至SLB'),
    )

    # git类型，就是在目标服务器上直接通过git clone/git pull的方式拉取代码部署
    # 比如python和php可以直接部署源码，那么可以直接在目标机器上git pull部署
    ARTIFACT_TYP_GIT = 'git'
    # 压缩包类型：将代码删除无用内容后，打成压缩包，存放到制品库，通过拉取压缩包的形式部署
    # 比如vue项目，通过build后，将dist目录打成压缩包，以后通过压缩包部署
    # 再或者java项目生成jar包后，也可以再打成压缩包来部署
    ARTIFACT_TYP_ARCHIVE = 'archive'
    # docker类型：通过生成docker镜像，推送到docker # hub.
    # 之后使用docker镜像部署(可以是部署在ECS，也可以是K8s)
    # 通过提供Dockerfile模板，生成docker镜像
    ARTIFACT_TYP_DOCKER = 'docker'
    ARTIFACT_TYP_CHOICES = (
        (ARTIFACT_TYP_GIT, 'git源码'),
        (ARTIFACT_TYP_ARCHIVE, '压缩包'),
        (ARTIFACT_TYP_DOCKER, 'Docker镜像'),
    )

    DEPLOY_TYP_ECS = 'ecs'
    DEPLOY_TYP_K8S = 'k8s'
    DEPLOY_TYP_CHOICES = (
        (DEPLOY_TYP_ECS, 'ECS部署'),
        (DEPLOY_TYP_K8S, 'K8s部署'),
    )

    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE, verbose_name='服务')
    environment = models.ForeignKey(EnvironmentModel, on_delete=models.CASCADE, verbose_name='环境')
    port = models.IntegerField('端口号', null=True)
    # 解析类型：代码服务使用的域名解析到哪里
    dns_typ = models.CharField('解析类型', max_length=128, choices=DNS_TYP_CHOICES)
    # 制品类型：制品就是我们部署什么东西，可以是直接git拉取源码、可以是一个压缩包、可以是docker镜像
    artifact_typ = models.CharField('制品类型', max_length=128, choices=ARTIFACT_TYP_CHOICES)
    # 部署类型：用来区分服务是直接部署在ECS上，还是部署到K8s上，或者通过docker部署
    # 可以根据自己的实际情况来增加类型
    deploy_typ = models.CharField('部署类型', max_length=128, choices=DEPLOY_TYP_CHOICES)

    class Meta:
        db_table = 'service_config'

    @classmethod
    def none_to_dict(cls):
        '''
        不存在时，返回内容
        '''
        data = {
            'port': None,
            'dns_typ': '',
            'dns_typ_desc': '',
            'artifact_typ': '',
            'artifact_typ_desc': '',
            'deploy_typ': '',
            'deploy_typ_desc': '',
        }
        return data
