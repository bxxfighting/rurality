from django.urls import path

from business.service.apis import deploy as deploy_api


urlpatterns = [
    path('service/publish/', deploy_api.PublishServiceApi.as_view()),
    path('service/restart/', deploy_api.RestartServiceApi.as_view()),
    path('service/rollback/', deploy_api.RollbackServiceApi.as_view()),
    path('service/deploy/config/', deploy_api.ServiceDeployConfigApi.as_view()),
]
