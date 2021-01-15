from django.urls import path

from business.service.apis import language as language_api


urlpatterns = [
    path('language/', language_api.LanguageApi.as_view()),
    path('language/list/', language_api.ListLanguageApi.as_view()),
    path('language/create/', language_api.CreateLanguageApi.as_view()),
    path('language/update/', language_api.UpdateLanguageApi.as_view()),
    path('language/delete/', language_api.DeleteLanguageApi.as_view()),
]
