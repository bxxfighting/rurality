from django.urls import path

from business.service.apis import domain as domain_api


urlpatterns = [
    path('service/domain/create/', domain_api.CreateServiceDomainApi.as_view()),
    path('service/domain/delete/', domain_api.DeleteServiceDomainApi.as_view()),
    path('service/domain/list/', domain_api.ListServiceDomainApi.as_view()),
]
