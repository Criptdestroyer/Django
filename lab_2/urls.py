from django.urls import path
from .views import index

#url for app, add your URL Configuration

urlpatterns = [
    path(r'^$', index, name='index'),
]
