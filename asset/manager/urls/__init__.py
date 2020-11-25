from asset.manager.urls import aliyun_key
from asset.manager.urls import asset


urlpatterns = aliyun_key.urlpatterns + \
              asset.urlpatterns
