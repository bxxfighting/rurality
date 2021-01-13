from component.gitlab.urls import server
from component.gitlab.urls import project


urlpatterns = server.urlpatterns + \
              project.urlpatterns
