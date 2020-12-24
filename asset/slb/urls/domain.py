from django.urls import path

from asset.slb.apis import domain as domain_api


urlpatterns = [
    path('slb/domain/list/', domain_api.ListSlbDomainApi.as_view()),
]
