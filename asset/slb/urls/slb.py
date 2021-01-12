from django.urls import path

from asset.slb.apis import slb as slb_api


urlpatterns = [
    path('slb/', slb_api.SlbApi.as_view()),
    path('slb/list/', slb_api.ListSlbApi.as_view()),
    path('slb/sync/', slb_api.SyncSlbApi.as_view()),
]
