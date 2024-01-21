from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('execute_dummy/', execute_dummy, name='execute_dummy'),
    path('execute_real/', execute_real, name='execute_real'),
    path('execute_history/', execute_history, name='execute_history'),
    path('execute_history_custom/', execute_history_custom, name='execute_history_custom'),
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("story_options/", views.story_options, name="story_options"),
    path("ai/", views.ai, name="ai"),
    path("history/", views.history, name="history"),
    path("real_posts/", views.real_posts, name="real_posts"),
]

from django.urls import path
from .views import execute_dummy