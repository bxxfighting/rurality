from asset.redis.urls import redis
from asset.redis.urls import account


urlpatterns = redis.urlpatterns + \
              account.urlpatterns
