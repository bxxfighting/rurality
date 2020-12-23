from django.urls import path

from asset.rds.apis import account as account_api


urlpatterns = [
    path('rds/account/', account_api.RdsAccountApi.as_view()),
    path('rds/account/list/', account_api.ListRdsAccountApi.as_view()),
    path('rds/account/update/', account_api.UpdateRdsAccountApi.as_view()),
    path('rds/account/database/list/', account_api.ListRdsAccountDatabaseApi.as_view()),
]
