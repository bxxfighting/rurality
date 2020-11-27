from django.urls import path

from business.service.apis import environment as environment_api


urlpatterns = [
    path('environment/', environment_api.EnvironmentApi.as_view()),
    path('environment/list/', environment_api.ListEnvironmentApi.as_view()),
    path('environment/create/', environment_api.CreateEnvironmentApi.as_view()),
    path('environment/update/', environment_api.UpdateEnvironmentApi.as_view()),
    path('environment/delete/', environment_api.DeleteEnvironmentApi.as_view()),
]
