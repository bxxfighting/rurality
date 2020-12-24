from django.urls import path

from asset.ecs.apis import domain as domain_api


urlpatterns = [
    path('ecs/domain/list/', domain_api.ListEcsDomainApi.as_view()),
]
