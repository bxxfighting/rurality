from asset.domain.urls import domain
from asset.domain.urls import record


urlpatterns = domain.urlpatterns + \
              record.urlpatterns
