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
    # Page for new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]