from django.urls import path

from asset.ecs.apis import ecs as ecs_api


urlpatterns = [
    path('ecs/', ecs_api.EcsApi.as_view()),
    path('ecs/list/', ecs_api.ListEcsApi.as_view()),
    path('ecs/service/list/', ecs_api.ListEcsServiceApi.as_view()),
    path('ecs/sync/', ecs_api.SyncEcsApi.as_view()),
]
