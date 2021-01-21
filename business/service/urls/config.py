from django.urls import path

from business.service.apis import config as config_api


urlpatterns = [
    path('service/config/', config_api.ServiceConfigApi.as_view()),
    path('service/config/update/', config_api.UpdateServiceConfigApi.as_view()),
]
