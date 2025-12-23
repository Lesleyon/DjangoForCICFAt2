from django.contrib import admin
from django.urls import path
from CICDproj import views
urlpatterns = [
    path('', views.home, name='home'),
]
