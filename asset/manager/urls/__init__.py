from asset.manager.urls import aliyun_key
from asset.manager.urls import asset
from asset.manager.urls import region


urlpatterns = aliyun_key.urlpatterns + \
              asset.urlpatterns + \
              region.urlpatterns
