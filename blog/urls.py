from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
# This code defines the URL patterns for the blog application.
# The `urlpatterns` list routes URLs to views.