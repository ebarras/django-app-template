from django.urls import path

from django_app_template.up import views


urlpatterns = [
    path("", views.index, name="index"),
    path("databases", views.databases, name="databases"),
]