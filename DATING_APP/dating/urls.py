from django.urls import path , include
from . import views 

urlpatterns = [
    path('',views.home, name = 'dating-home'),
    path('dashboard/',views.dashboard, name = 'dating-dashboard'),
    path('dashboard/like', views.dashboard_like, name='like-user'),
    path('interests/',views.Interests, name = 'dating-interests'),
    path('interests/add-music', views.add_music, name = 'interest-add-music'),
    path('pending', views.pending, name = 'dating-pending'),
    path('pending/match', views.match_user, name='pending-match-user')
]


