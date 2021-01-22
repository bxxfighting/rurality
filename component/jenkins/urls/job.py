from django.urls import path

from component.jenkins.apis import job as job_api


urlpatterns = [
    path('jenkins/job/list/', job_api.ListJenkinsJobApi.as_view()),
    path('jenkins/job/sync/', job_api.SyncJenkinsJobApi.as_view()),
]
