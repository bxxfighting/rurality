from business.project import urls as project_url
from business.service import urls as service_url


urlpatterns = project_url.urlpatterns + \
              service_url.urlpatterns
