from django.urls import path

from asset.rds.apis import rds as rds_api


urlpatterns = [
    path('rds/', rds_api.RdsApi.as_view()),
    path('rds/list/', rds_api.ListRdsApi.as_view()),
    path('rds/sync/', rds_api.SyncRdsApi.as_view()),
]
