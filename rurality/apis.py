from base.api import BaseApi


class HealthApi(BaseApi):
    NEED_LOGIN = False

    need_params = {
    }
    def get(self, request, params):
        # TODO: 检查所需组件的可访问状态
        # mysql、redis等
        return 'ok'
