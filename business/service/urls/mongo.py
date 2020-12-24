from django.urls import path

from business.service.apis import mongo as mongo_api


urlpatterns = [
    path('service/mongo/create/', mongo_api.CreateServiceMongoApi.as_view()),
    path('service/mongo/delete/', mongo_api.DeleteServiceMongoApi.as_view()),
    path('service/mongo/list/', mongo_api.ListServiceMongoApi.as_view()),
]
