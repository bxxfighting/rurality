from asset.ecs.urls import ecs
from asset.ecs.urls import domain


urlpatterns = ecs.urlpatterns + \
              domain.urlpatterns
