from django.urls import path

from component.gitlab.apis import server as server_api


urlpatterns = [
    path('gitlab/server/', server_api.GitlabServerApi.as_view()),
    path('gitlab/server/list/', server_api.ListGitlabServerApi.as_view()),
    path('gitlab/server/create/', server_api.CreateGitlabServerApi.as_view()),
    path('gitlab/server/update/', server_api.UpdateGitlabServerApi.as_view()),
    path('gitlab/server/delete/', server_api.DeleteGitlabServerApi.as_view()),
]
