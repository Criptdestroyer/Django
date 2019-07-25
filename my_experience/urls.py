from django.urls import path
from my_experience.views import index

#url for app, add your URL Configuration

urlpatterns = [
    path('', index, name='index'),
]
