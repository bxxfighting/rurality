from component.gitlab import urls as gitlab_urls
from component.jenkins import urls as jenkins_urls
from component.ldap import urls as ldap_urls


urlpatterns = gitlab_urls.urlpatterns + \
              jenkins_urls.urlpatterns + \
              ldap_urls.urlpatterns
