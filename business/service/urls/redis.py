from django.urls import path

from business.service.apis import redis as redis_api


urlpatterns = [
    path('service/redis/create/', redis_api.CreateServiceRedisApi.as_view()),
    path('service/redis/delete/', redis_api.DeleteServiceRedisApi.as_view()),
    path('service/redis/list/', redis_api.ListServiceRedisApi.as_view()),
]
