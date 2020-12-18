from asset.slb.urls import slb
from asset.slb.urls import server_group


urlpatterns = slb.urlpatterns + \
              server_group.urlpatterns 
