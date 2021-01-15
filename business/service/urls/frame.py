from django.urls import path

from business.service.apis import frame as frame_api


urlpatterns = [
    path('frame/', frame_api.FrameApi.as_view()),
    path('frame/list/', frame_api.ListFrameApi.as_view()),
    path('frame/create/', frame_api.CreateFrameApi.as_view()),
    path('frame/update/', frame_api.UpdateFrameApi.as_view()),
    path('frame/delete/', frame_api.DeleteFrameApi.as_view()),
]
