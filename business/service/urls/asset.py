from django.urls import path

from business.service.apis import asset as asset_api


urlpatterns = [
    path('service/asset/create/', asset_api.CreateServiceAssetApi.as_view()),
    path('service/asset/delete/', asset_api.DeleteServiceAssetApi.as_view()),
    path('service/asset/list/', asset_api.ListServiceAssetApi.as_view()),
]
