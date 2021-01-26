from base.api import BaseApi
from business.service.controllers import deploy as deploy_ctl


class PublishServiceApi(BaseApi):

    need_params = {
        'service_id': ('服务ID', 'required int'),
        'environment_id': ('环境ID', 'required int'),
        'publish_typ': ('发布类型', 'required str 128'),
        'ecs_ids': ('ECS列表', 'optional list'),
        'version_typ': ('版本类型', 'required str 128'),
        'version': ('版本号', 'required str 128'),
        'time_mode': ('时间模式', 'required int'),
        'dt_start': ('开始时间', 'optional datetime'),
    }
    def post(self, request, params):
        deploy_ctl.publish_service(**params)


class RestartServiceApi(BaseApi):

    need_params = {
        'service_id': ('服务ID', 'required int'),
        'environment_id': ('环境ID', 'required int'),
        'publish_typ': ('发布类型', 'required str 128'),
        'ecs_ids': ('ECS列表', 'optional list'),
        'time_mode': ('时间模式', 'required int'),
        'dt_start': ('开始时间', 'optional datetime'),
    }
    def post(self, request, params):
        deploy_ctl.restart_service(**params)


class RollbackServiceApi(BaseApi):

    need_params = {
        'service_id': ('服务ID', 'required int'),
        'environment_id': ('环境ID', 'required int'),
        'publish_typ': ('发布类型', 'required str 128'),
        'ecs_ids': ('ECS列表', 'optional list'),
        'version': ('版本号', 'required str 128'),
        'time_mode': ('时间模式', 'required int'),
        'dt_start': ('开始时间', 'optional datetime'),
    }
    def post(self, request, params):
        deploy_ctl.rollback_service(**params)
