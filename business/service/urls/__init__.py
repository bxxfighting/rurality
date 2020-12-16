from business.service.urls import service
from business.service.urls import environment
from business.service.urls import asset
from business.service.urls import ecs


urlpatterns = service.urlpatterns + \
              environment.urlpatterns + \
              asset.urlpatterns + \
              ecs.urlpatterns
