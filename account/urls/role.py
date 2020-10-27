from django.urls import path

from account.apis import role as role_api


urlpatterns = [
    path('role/', role_api.RoleApi.as_view()),
    path('role/list/', role_api.ListRoleApi.as_view()),
    path('role/create/', role_api.CreateRoleApi.as_view()),
    path('role/update/', role_api.UpdateRoleApi.as_view()),
    path('role/delete/', role_api.DeleteRoleApi.as_view()),
]
