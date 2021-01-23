from account.urls import user
from account.urls import role
from account.urls import mod
from account.urls import department
from account.urls import permission
from account.urls import ldap


urlpatterns = user.urlpatterns + \
              role.urlpatterns + \
              mod.urlpatterns + \
              department.urlpatterns + \
              permission.urlpatterns + \
              ldap.urlpatterns
