from account.urls import user
from account.urls import mod
from account.urls import permission


urlpatterns = user.urlpatterns + \
              mod.urlpatterns + \
              permission.urlpatterns
