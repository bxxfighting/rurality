from asset.manager import urls as manager_urls
from asset.ecs import urls as ecs_urls


urlpatterns = manager_urls.urlpatterns + \
              ecs_urls.urlpatterns
