from django.urls import path

from asset.mongo.apis import account as account_api


urlpatterns = [
    path('mongo/account/', account_api.MongoAccountApi.as_view()),
    path('mongo/account/list/', account_api.ListMongoAccountApi.as_view()),
    path('mongo/account/update/', account_api.UpdateMongoAccountApi.as_view()),
]
