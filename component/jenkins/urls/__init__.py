from component.jenkins.urls import server
from component.jenkins.urls import job


urlpatterns = server.urlpatterns + \
              job.urlpatterns
