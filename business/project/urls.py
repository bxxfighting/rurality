from django.urls import path

from business.project import apis as project_api


urlpatterns = [
    path('project/', project_api.ProjectApi.as_view()),
    path('project/list/', project_api.ListProjectApi.as_view()),
    path('project/create/', project_api.CreateProjectApi.as_view()),
    path('project/update/', project_api.UpdateProjectApi.as_view()),
    path('project/delete/', project_api.DeleteProjectApi.as_view()),
    path('project/user/create/', project_api.CreateProjectUserApi.as_view()),
    path('project/user/update/', project_api.UpdateProjectUserApi.as_view()),
    path('project/user/delete/', project_api.DeleteProjectUserApi.as_view()),
    path('project/user/list/', project_api.ListProjectUserApi.as_view()),
    path('project/service/list/', project_api.ListProjectServiceApi.as_view()),
]
