from django.urls import path

from asset.redis.apis import account as account_api


urlpatterns = [
    path('redis/account/', account_api.RedisAccountApi.as_view()),
    path('redis/account/list/', account_api.ListRedisAccountApi.as_view()),
    path('redis/account/update/', account_api.UpdateRedisAccountApi.as_view()),
]
