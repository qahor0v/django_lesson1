from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index1"),
    path(".", views.index, name="index"),
]