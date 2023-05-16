from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path("points", views.points, name="points"),
    path("linear", views.linear, name="linear"),
    path("quadratic", views.quadratic, name="quadratic"),
]
