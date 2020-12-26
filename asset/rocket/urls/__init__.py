from asset.rocket.urls import rocket
from asset.rocket.urls import topic
from asset.rocket.urls import group


urlpatterns = rocket.urlpatterns + \
              topic.urlpatterns + \
              group.urlpatterns
