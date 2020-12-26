from django.urls import path

from business.service.apis import rocket_topic as rocket_topic_api


urlpatterns = [
    path('service/rocket/topic/create/', rocket_topic_api.CreateServiceRocketTopicApi.as_view()),
    path('service/rocket/topic/delete/', rocket_topic_api.DeleteServiceRocketTopicApi.as_view()),
    path('service/rocket/topic/list/', rocket_topic_api.ListServiceRocketTopicApi.as_view()),
]
