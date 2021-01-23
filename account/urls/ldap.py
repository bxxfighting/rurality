from django.urls import path

from account.apis import ldap as ldap_api


urlpatterns = [
    path('ldap/config/', ldap_api.LdapConfigApi.as_view()),
    path('ldap/config/update/', ldap_api.UpdateLdapConfigApi.as_view()),
    path('ldap/user/sync/', ldap_api.SyncLdapUserApi.as_view()),
]
