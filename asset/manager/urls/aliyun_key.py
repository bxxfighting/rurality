from django.urls import path

from asset.manager.apis import aliyun_key as aliyun_key_api


urlpatterns = [
    path('aliyun_key/', aliyun_key_api.AliyunKeyApi.as_view()),
    path('aliyun_key/list/', aliyun_key_api.ListAliyunKeyApi.as_view()),
    path('aliyun_key/create/', aliyun_key_api.CreateAliyunKeyApi.as_view()),
    path('aliyun_key/update/', aliyun_key_api.UpdateAliyunKeyApi.as_view()),
    path('aliyun_key/delete/', aliyun_key_api.DeleteAliyunKeyApi.as_view()),
    path('aliyun_key/status/set/', aliyun_key_api.SetAliyunKeyStatusApi.as_view()),
]
