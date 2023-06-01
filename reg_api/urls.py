from django.urls import path
from . import regression_views, modification_views, data_views

urlpatterns = [
    path("points", data_views.points, name="points"),
    path("points/<int:pk>", data_views.point, name="point"),
    path("points/<int:pk>/patch", modification_views.patch, name="patch"),
    path("linear", regression_views.linear, name="linear"),
    path("quadratic", regression_views.quadratic, name="quadratic"),
    path("ridge", regression_views.ridge, name="ridge"),
    path("add", modification_views.post, name="post"),
]
