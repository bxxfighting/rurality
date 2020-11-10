from django.urls import path

from business.service import apis as service_api


urlpatterns = [
    path('service/', service_api.ServiceApi.as_view()),
    path('service/list/', service_api.ListServiceApi.as_view()),
    path('service/create/', service_api.CreateServiceApi.as_view()),
    path('service/update/', service_api.UpdateServiceApi.as_view()),
    path('service/delete/', service_api.DeleteServiceApi.as_view()),
    path('service/department/create/', service_api.CreateServiceDepartmentApi.as_view()),
    path('service/department/delete/', service_api.DeleteServiceDepartmentApi.as_view()),
    path('service/department/list/', service_api.ListServiceDepartmentApi.as_view()),
    path('service/user/create/', service_api.CreateServiceUserApi.as_view()),
    path('service/user/update/', service_api.UpdateServiceUserApi.as_view()),
    path('service/user/delete/', service_api.DeleteServiceUserApi.as_view()),
    path('service/user/list/', service_api.ListServiceUserApi.as_view()),
]
