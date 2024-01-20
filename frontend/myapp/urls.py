from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("contact/", views.contact, name="contact"),
    path("todos/", views.todos, name="todos"),
    # path('my-form/', views.contentForm, name='dropdown_processor')
    path('', views.dropdownsearch, name='dropdownsearch'),
]