from business.service.urls import service
from business.service.urls import environment
from business.service.urls import asset


urlpatterns = service.urlpatterns + \
              environment.urlpatterns + \
              asset.urlpatterns
