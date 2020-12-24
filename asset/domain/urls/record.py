from django.urls import path

from asset.domain.apis import record as record_api


urlpatterns = [
    path('domain/record/', record_api.DomainRecordApi.as_view()),
    path('domain/record/list/', record_api.ListDomainRecordApi.as_view()),
    path('domain/record/service/list/', record_api.ListDomainRecordServiceApi.as_view()),
]
