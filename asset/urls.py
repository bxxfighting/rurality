from asset.manager import urls as manager_urls
from asset.ecs import urls as ecs_urls
from asset.slb import urls as slb_urls
from asset.rds import urls as rds_urls
from asset.redis import urls as redis_urls
from asset.mongo import urls as mongo_urls


urlpatterns = manager_urls.urlpatterns + \
              ecs_urls.urlpatterns + \
              slb_urls.urlpatterns + \
              rds_urls.urlpatterns + \
              redis_urls.urlpatterns + \
              mongo_urls.urlpatterns
