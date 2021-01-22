from django.urls import path

from component.jenkins.apis import server as server_api


urlpatterns = [
    path('jenkins/server/', server_api.JenkinsServerApi.as_view()),
    path('jenkins/server/list/', server_api.ListJenkinsServerApi.as_view()),
    path('jenkins/server/create/', server_api.CreateJenkinsServerApi.as_view()),
    path('jenkins/server/update/', server_api.UpdateJenkinsServerApi.as_view()),
    path('jenkins/server/delete/', server_api.DeleteJenkinsServerApi.as_view()),
]
