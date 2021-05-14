from django.contrib import admin
from django.urls import path, include
from interconnect import views

urlpatterns = [
    path('', views.index, name='home'),
    path('rtsp_feed', views.rtsp_feed, name='rtsp_feed'),
]
