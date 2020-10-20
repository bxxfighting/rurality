from django.urls import path

from account.apis import user as user_api


urlpatterns = [
    path('user/login/', user_api.LoginApi.as_view()),
]
