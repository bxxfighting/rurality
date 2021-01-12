from django.urls import path

from asset.rocket.apis import rocket as rocket_api


urlpatterns = [
    path('rocket/', rocket_api.RocketApi.as_view()),
    path('rocket/list/', rocket_api.ListRocketApi.as_view()),
    path('rocket/sync/', rocket_api.SyncRocketApi.as_view()),
]
