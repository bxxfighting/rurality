from django.urls import path

from account.apis import mod as mod_api


urlpatterns = [
    path('mod/', mod_api.ModApi.as_view()),
    path('mod/list/', mod_api.ListModApi.as_view()),
    path('mod/create/', mod_api.CreateModApi.as_view()),
    path('mod/update/', mod_api.UpdateModApi.as_view()),
    path('mod/delete/', mod_api.DeleteModApi.as_view()),
]
