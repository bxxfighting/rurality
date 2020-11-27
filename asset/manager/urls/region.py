from django.urls import path

from asset.manager.apis import region as region_api


urlpatterns = [
    path('region/', region_api.RegionApi.as_view()),
    path('region/list/', region_api.ListRegionApi.as_view()),
    path('region/status/set/', region_api.SetRegionStatusApi.as_view()),
    path('zone/', region_api.ZoneApi.as_view()),
    path('zone/list/', region_api.ListZoneApi.as_view()),
]
