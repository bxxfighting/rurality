from asset.mongo.urls import mongo
from asset.mongo.urls import account


urlpatterns = mongo.urlpatterns + \
              account.urlpatterns
