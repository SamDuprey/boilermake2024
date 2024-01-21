from django.urls import path
from . import views
from .views import execute_dummy

urlpatterns = [
    path('execute_dummy/', execute_dummy, name='execute_dummy'),
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("options/", views.options, name="options"),
    path("story_options/", views.story_options, name="story_options"),
    path("ai/", views.ai, name="ai"),
]

from django.urls import path
from .views import execute_dummy