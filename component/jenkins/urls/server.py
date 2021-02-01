from django.urls import path

from component.jenkins.apis import server as server_api


urlpatterns = [
    path('jenkins/server/', server_api.JenkinsServerApi.as_view()),
    path('jenkins/server/update/', server_api.UpdateJenkinsServerApi.as_view()),
]
