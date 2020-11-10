from django.urls import path

from account.apis import department as department_api


urlpatterns = [
    path('department/', department_api.DepartmentApi.as_view()),
    path('department/list/', department_api.ListDepartmentApi.as_view()),
    path('department/create/', department_api.CreateDepartmentApi.as_view()),
    path('department/update/', department_api.UpdateDepartmentApi.as_view()),
    path('department/delete/', department_api.DeleteDepartmentApi.as_view()),
    path('department/user/create/', department_api.CreateDepartmentUserApi.as_view()),
    path('department/user/update/', department_api.UpdateDepartmentUserApi.as_view()),
    path('department/user/delete/', department_api.DeleteDepartmentUserApi.as_view()),
    path('department/user/list/', department_api.ListDepartmentUserApi.as_view()),
    path('department/service/list/', department_api.ListDepartmentServiceApi.as_view()),
]
