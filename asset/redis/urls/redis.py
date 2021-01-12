from django.urls import path

from asset.redis.apis import redis as redis_api


urlpatterns = [
    path('redis/', redis_api.RedisApi.as_view()),
    path('redis/list/', redis_api.ListRedisApi.as_view()),
    path('redis/sync/', redis_api.SyncRedisApi.as_view()),
    path('redis/service/list/', redis_api.ListRedisServiceApi.as_view()),
]
