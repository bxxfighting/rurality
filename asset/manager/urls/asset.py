from django.urls import path

from asset.manager.apis import asset as asset_api


urlpatterns = [
    path('', asset_api.AssetApi.as_view()),
    path('list/', asset_api.ListAssetApi.as_view()),
    path('create/', asset_api.CreateAssetApi.as_view()),
    path('update/', asset_api.UpdateAssetApi.as_view()),
    path('delete/', asset_api.DeleteAssetApi.as_view()),
]
