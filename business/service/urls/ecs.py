from django.urls import path

from business.service.apis import ecs as ecs_api


urlpatterns = [
    path('service/ecs/create/', ecs_api.CreateServiceEcsApi.as_view()),
    path('service/ecs/delete/', ecs_api.DeleteServiceEcsApi.as_view()),
    path('service/ecs/list/', ecs_api.ListServiceEcsApi.as_view()),
]
