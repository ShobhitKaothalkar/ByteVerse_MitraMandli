from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name = 'spotify_test_home'),
]