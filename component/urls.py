from component.gitlab import urls as gitlab_urls
from component.jenkins import urls as jenkins_urls


urlpatterns = gitlab_urls.urlpatterns + \
              jenkins_urls.urlpatterns
