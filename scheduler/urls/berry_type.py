from django.urls import path

from scheduler.apis import berry_type as berry_type_api


urlpatterns = [
    path('berry/type/', berry_type_api.BerryTypeApi.as_view()),
    path('berry/type/list/', berry_type_api.ListBerryTypeApi.as_view()),
    path('berry/type/create/', berry_type_api.CreateBerryTypeApi.as_view()),
    path('berry/type/update/', berry_type_api.UpdateBerryTypeApi.as_view()),
    path('berry/type/delete/', berry_type_api.DeleteBerryTypeApi.as_view()),
]
