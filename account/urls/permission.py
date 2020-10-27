from django.urls import path

from account.apis import permission as permission_api


urlpatterns = [
    path('permission/', permission_api.PermissionApi.as_view()),
    path('permission/list/', permission_api.ListPermissionApi.as_view()),
    path('permission/create/', permission_api.CreatePermissionApi.as_view()),
    path('permission/update/', permission_api.UpdatePermissionApi.as_view()),
    path('permission/delete/', permission_api.DeletePermissionApi.as_view()),
]
