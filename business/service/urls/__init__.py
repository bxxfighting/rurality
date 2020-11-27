from business.service.urls import service
from business.service.urls import environment


urlpatterns = service.urlpatterns + \
              environment.urlpatterns
