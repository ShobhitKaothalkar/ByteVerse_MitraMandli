from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
from .models import CustomUser
from .models import Interests
from .models import MusicProfile



admin.site.register(CustomUser)

admin.site.register(UserProfile)

admin.site.register(Interests)

admin.site.register(MusicProfile)
