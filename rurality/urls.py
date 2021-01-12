from django.urls import path
from django.urls import include

from rurality.apis import HealthApi


urlpatterns = [
    path('api/v1/', include({
        path('account/', include('account.urls')),
        path('business/', include('business.urls')),
        path('asset/', include('asset.urls')),
        path('scheduler/', include('scheduler.urls')),
    })),
    path('health/', HealthApi.as_view()),
]
