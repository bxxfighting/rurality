from django.db import models
from base.models import BaseModel


class RocketModel(BaseModel):
    '''
    RocketMQ
    '''
    model_name = 'Rocket'
    model_sign = 'rocket'

    instance_id = models.CharField('实例id', max_length=128)
    name = models.CharField('名称', max_length=128)
    is_independent_naming = models.BooleanField('是否命名独立空间')
    region_id = models.CharField('地域', max_length=128)

    class Meta:
        db_table = 'rocket'

    @property
    def web_url(self):
        host = 'https://ons.console.aliyun.com'
        url = f'{host}/region/{self.region_id}/instance/{self.instance_id}/detail'
        return url

    def to_dict(self):
        data = super().to_dict()
        data['web_url'] = self.web_url
        return data


class RocketTopicModel(BaseModel):
    '''
    RocketMQ Topic
    '''
    model_name = 'RocketMQ Topic'
    model_sign = 'rocket_topic'

    rocket = models.ForeignKey(RocketModel, on_delete=models.CASCADE)
    name = models.CharField('名称', max_length=128)
    remark = models.TextField('备注')

    class Meta:
        db_table = 'rocket_topic'

    @property
    def web_url(self):
        prefix = self.rocket.web_url.split('detail')[0]
        url = f'{prefix}topic/TOPIC_ketang_goim_mids/detail'
        return url

    def to_dict(self, is_base=True):
        data = super().to_dict()
        data['web_url'] = self.web_url
        if not is_base:
            data['rocket'] = self.rocket.to_dict()
        return data


class RocketGroupModel(BaseModel):
    '''
    RocketMQ Group
    '''
    model_name = 'RocketMQ Group'
    model_sign = 'rocket_group'

    rocket = models.ForeignKey(RocketModel, on_delete=models.CASCADE)
    name = models.CharField('名称', max_length=128)
    typ = models.CharField('类型', max_length=128)
    remark = models.TextField('备注')

    class Meta:
        db_table = 'rocket_group'


class RocketGroupTopicModel(BaseModel):
    '''
    RocketMQ Group
    '''
    model_name = 'RocketMQ Group订阅Topic'
    model_sign = 'rocket_group_topic'

    rocket = models.ForeignKey(RocketModel, on_delete=models.CASCADE)
    group = models.ForeignKey(RocketGroupModel, on_delete=models.CASCADE)
    topic = models.ForeignKey(RocketTopicModel, on_delete=models.CASCADE)
    exp = models.TextField('订阅表达式')

    class Meta:
        db_table = 'rocket_group_topic'
