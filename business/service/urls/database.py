from django.urls import path

from business.service.apis import database as database_api


urlpatterns = [
    path('service/database/create/', database_api.CreateServiceDatabaseApi.as_view()),
    path('service/database/delete/', database_api.DeleteServiceDatabaseApi.as_view()),
    path('service/database/list/', database_api.ListServiceDatabaseApi.as_view()),
]
