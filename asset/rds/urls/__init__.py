from asset.rds.urls import rds
from asset.rds.urls import database
from asset.rds.urls import account


urlpatterns = rds.urlpatterns + \
              database.urlpatterns + \
              account.urlpatterns
