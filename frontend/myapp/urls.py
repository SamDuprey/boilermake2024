from django.urls import path
from . import views
from .views import execute_dummy

urlpatterns = [
    path('execute_dummy/', execute_dummy, name='execute_dummy'),
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
]

from django.urls import path
from .views import execute_dummy