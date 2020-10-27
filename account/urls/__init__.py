from account.urls import user
from account.urls import mod


urlpatterns = user.urlpatterns + \
              mod.urlpatterns
