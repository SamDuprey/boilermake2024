from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('execute_dummy/', execute_dummy, name='execute_dummy'),
    path('execute_video/', execute_video, name='execute_video'),
    path('execute_real/', execute_real, name='execute_real'),
    path('execute_history/', execute_history, name='execute_history'),
    path('execute_custom/', execute_custom, name='execute_custom'),
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("story_options/", views.story_options, name="story_options"),
    path("ai/", views.ai, name="ai"),
    path("history/", views.history, name="history"),
    path("real_posts/", views.real_posts, name="real_posts"),
    path("custom/", views.custom, name="custom"),
    path("history_options/", views.history_options, name="history_options"),
    path("history_custom/", views.history_custom, name="history_custom"),
    path('download_video/', download_video, name='download_video'),
]

from django.urls import path
from .views import execute_dummy