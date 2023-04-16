from django.contrib import admin
from django.urls import path , include
from users import views as userViews
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',include('dating.urls')),
    path('chat/', include('chat.urls')),
    path('admin/', admin.site.urls),
    path('register/', userViews.register , name = 'register'),
    path('register/create-profile', userViews.createProfile , name = 'create-profile'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html', redirect_authenticated_user=True) , name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html') , name = 'logout'),
]

# urlpatterns = [

# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
