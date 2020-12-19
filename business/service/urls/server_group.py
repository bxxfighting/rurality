from django.urls import path

from business.service.apis import server_group as server_group_api


urlpatterns = [
    path('service/server/group/create/', server_group_api.CreateServiceServerGroupApi.as_view()),
    path('service/server/group/delete/', server_group_api.DeleteServiceServerGroupApi.as_view()),
    path('service/server/group/list/', server_group_api.ListServiceServerGroupApi.as_view()),
]
