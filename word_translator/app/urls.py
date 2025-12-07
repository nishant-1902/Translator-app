from django.contrib import admin
from django.urls import path
from . import views   # import views from the same app

urlpatterns = [
    path('', views.home, name="home"),
]
