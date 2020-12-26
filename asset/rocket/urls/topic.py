from django.urls import path

from asset.rocket.apis import topic as topic_api


urlpatterns = [
    path('rocket/topic/', topic_api.RocketTopicApi.as_view()),
    path('rocket/topic/list/', topic_api.ListRocketTopicApi.as_view()),
]
