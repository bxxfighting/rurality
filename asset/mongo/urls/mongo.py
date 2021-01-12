from django.urls import path

from asset.mongo.apis import mongo as mongo_api


urlpatterns = [
    path('mongo/', mongo_api.MongoApi.as_view()),
    path('mongo/list/', mongo_api.ListMongoApi.as_view()),
    path('mongo/sync/', mongo_api.SyncMongoApi.as_view()),
    path('mongo/service/list/', mongo_api.ListMongoServiceApi.as_view()),
]
