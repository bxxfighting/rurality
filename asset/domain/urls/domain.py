from django.urls import path

from asset.domain.apis import domain as domain_api


urlpatterns = [
    path('domain/', domain_api.DomainApi.as_view()),
    path('domain/list/', domain_api.ListDomainApi.as_view()),
    path('domain/sync/', domain_api.SyncDomainApi.as_view()),
]
