from django.urls import path

from account.apis import role as role_api


urlpatterns = [
    path('role/', role_api.RoleApi.as_view()),
    path('role/list/', role_api.ListRoleApi.as_view()),
    path('role/create/', role_api.CreateRoleApi.as_view()),
    path('role/update/', role_api.UpdateRoleApi.as_view()),
    path('role/delete/', role_api.DeleteRoleApi.as_view()),
    path('role/user/create/', role_api.CreateRoleUserApi.as_view()),
    path('role/user/delete/', role_api.DeleteRoleUserApi.as_view()),
    path('role/user/list/', role_api.ListRoleUserApi.as_view()),
    path('role/mod/create/', role_api.CreateRoleModApi.as_view()),
    path('role/mod/delete/', role_api.DeleteRoleModApi.as_view()),
    path('role/mod/list/', role_api.ListRoleModApi.as_view()),
    path('role/permission/create/', role_api.CreateRolePermissionApi.as_view()),
    path('role/permission/delete/', role_api.DeleteRolePermissionApi.as_view()),
    path('role/permission/list/', role_api.ListRolePermissionApi.as_view()),
]
