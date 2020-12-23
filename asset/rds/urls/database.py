from django.urls import path

from asset.rds.apis import database as database_api


urlpatterns = [
    path('rds/database/', database_api.RdsDatabaseApi.as_view()),
    path('rds/database/list/', database_api.ListRdsDatabaseApi.as_view()),
    path('rds/database/account/list/', database_api.ListRdsDatabaseAccountApi.as_view()),
    path('rds/database/service/list/', database_api.ListRdsDatabaseServiceApi.as_view()),
]
