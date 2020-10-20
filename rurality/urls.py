from django.urls import path
from django.urls import include


urlpatterns = [
    path('api/v1/', include({
        path('account/', include('account.urls')),
    }))
]
