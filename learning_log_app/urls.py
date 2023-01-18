"""Defines URL patterns for learning_log_app"""

from django.urls import path

from . import views

app_name = 'learning_log_app'
urlpatterns = [
    # Main page
    path('', views.index, name='index'),
    # Topic page
    path('topic/', views.topics, name='topics'),
    # Page for each topic
    path('topic/<int:topic_id>/', views.topic, name='topic'),
]