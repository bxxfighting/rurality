from django.urls import path

from asset.slb.apis import server_group as server_group_api


urlpatterns = [
    path('slb/server/group/', server_group_api.ServerGroupApi.as_view()),
    path('slb/server/group/list/', server_group_api.ListServerGroupApi.as_view()),
    path('slb/server/group/ecs/list/', server_group_api.ListServerGroupEcsApi.as_view()),
    path('slb/server/group/service/list/', server_group_api.ListServerGroupServiceApi.as_view()),
]
