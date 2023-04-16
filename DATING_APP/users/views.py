from django.shortcuts import render  , redirect
from .forms import UserRegisterForm , UserProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .backends import EmailBackend
from django.contrib.auth import authenticate, login
from .models import Interests

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('dating-home')
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.set_password(new_user.password)
            messages.info(request, "Thanks for registering. You are now logged in.")
            new_user = authenticate(request, username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'],
                                    backend=EmailBackend)
            new_user.is_active = True
            new_user.save()
            login(request, new_user)
            return redirect('create-profile')
    else:
        form  = UserRegisterForm()
    return render(request , 'users/register.html' ,{ 'form' : form})


@login_required
def createProfile(request):
    print(request.user.has_profile)
    if request.user.has_profile == True:
        return redirect('dating-home')
    if request.method =='POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            user_interests = Interests.objects.create(profile=profile)
            request.user.has_profile = True
            request.user.save()
            return redirect('dating-dashboard')
    else:
        form  = UserProfileForm()
    return render(request , 'users/createProfile.html' ,{ 'form' : form})

