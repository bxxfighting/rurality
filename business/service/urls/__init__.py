from business.service.urls import service
from business.service.urls import environment
from business.service.urls import asset
from business.service.urls import ecs
from business.service.urls import server_group
from business.service.urls import database


urlpatterns = service.urlpatterns + \
              environment.urlpatterns + \
              asset.urlpatterns + \
              ecs.urlpatterns + \
              server_group.urlpatterns + \
              database.urlpatterns
