from asset.slb.urls import slb
from asset.slb.urls import server_group
from asset.slb.urls import domain


urlpatterns = slb.urlpatterns + \
              server_group.urlpatterns + \
              domain.urlpatterns 
