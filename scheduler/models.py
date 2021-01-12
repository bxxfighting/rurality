from django.db import models
from base.models import BaseModel


class BerryTypeModel(BaseModel):
    '''
    Berry类型
    '''
    model_name = '任务类型'
    model_sign = 'berry_type'

    name = models.CharField('名称', max_length=128)
    sign = models.CharField('标识', max_length=128)
    parent_id = models.IntegerField('父级ID', null=True)

    class Meta:
        db_table = 'berry_type'


class BerryModel(BaseModel):
    '''
    Ferry是摆渡，Berry就是卜摆渡
    '''
    model_name = '任务'
    model_sign = 'berry'

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

    # 代表结束状态
    END_STATUS = (ST_SUCCESS, ST_FAILURE, ST_ABORTED, ST_CANCELLED,)

    TIME_MODE_NOW = 10
    TIME_MODE_CRONTAB = 20
    TIME_MODE_CHOICES = (
        (TIME_MODE_NOW, '立即执行'),
        (TIME_MODE_CRONTAB, '定时执行'),
    )

    RUN_MODE_NORMAL = 10
    RUN_MODE_CYCLE = 20
    RUN_MODE_CHOICES = (
        (RUN_MODE_NORMAL, '标准任务'),
        (RUN_MODE_CYCLE, '周期任务'),
    )

    parent_id = models.IntegerField('父任务ID', null=True, default=None)
    name = models.CharField('名称', max_length=128)
    task_id = models.CharField('任务ID', max_length=128)
    status = models.SmallIntegerField('状态', choices=ST_CHOICES, default=ST_PENDING)
    typ = models.ForeignKey(BerryTypeModel, on_delete=models.CASCADE)
    run_mode = models.SmallIntegerField('运行模式', choices=RUN_MODE_CHOICES, default=RUN_MODE_NORMAL)
    time_mode = models.SmallIntegerField('时间模式', choices=TIME_MODE_CHOICES)
    # input_params、output_params一般存入json.dumps后的数据
    # 记录任务运行需要使用到的数据
    input_params = models.TextField('输入参数', null=True, default=None)
    # 记录任务结束后可以提供的数据
    output_params = models.TextField('输出参数', null=True, default=None)
    # 任务开始时间
    dt_start = models.DateTimeField('开始时间', null=True, default=None)
    # 任务结束时间
    dt_end = models.DateTimeField('结束时间', null=True, default=None)
    duration = models.IntegerField('执行用时(s)', null=True, default=None)
    # 如果失败则记录错误日志
    error_log = models.TextField('错误日志', null=True, default=None)

    class Meta:
        db_table = 'berry'
