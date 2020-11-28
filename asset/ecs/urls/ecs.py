from django.urls import path

from asset.ecs.apis import ecs as ecs_api


urlpatterns = [
    path('ecs/', ecs_api.EcsApi.as_view()),
    path('ecs/list/', ecs_api.ListEcsApi.as_view()),
]
