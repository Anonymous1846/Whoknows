from django.urls import path
from .views import MainView,TopicView,CreateTopicView,DeleteTopic
urlpatterns = [
    path('',MainView.as_view(),name='home'),
    path('topic/<int:pk>',TopicView.as_view(),name='topic-detail'),
    path('delete/<int:pk>',DeleteTopic.as_view(),name='delete-topic'),
    path('new/',CreateTopicView.as_view(),name='new-topic')
]
