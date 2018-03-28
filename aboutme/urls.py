from django.contrib import admin
from django.conf.urls import include
from django.urls import path

from .views import main_view


urlpatterns = [
    path('', main_view, name='main')
]
