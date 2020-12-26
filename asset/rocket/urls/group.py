from django.urls import path

from asset.rocket.apis import group as group_api


urlpatterns = [
    path('rocket/group/', group_api.RocketGroupApi.as_view()),
    path('rocket/group/list/', group_api.ListRocketGroupApi.as_view()),
]
