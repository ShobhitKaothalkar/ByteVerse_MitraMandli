from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .spotifyapi import getUserSpotifyInfo
from users.models import MusicProfile, CustomUser
from .forms import InterestSelectionForm
import pandas as pd
from .clustering import generate_recommendations
from django.http import HttpResponse
import json
from chat.models import Thread

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('dating-dashboard')
    return render(request , 'dating/home.html')

@login_required
def dashboard(request):
    form = InterestSelectionForm()
    if request.GET.get('interest') == 'Music':
        data = {"myindex": [], "user_ID": [], "genres": [], "popularity": [], "duration": []}
        users = CustomUser.objects.all()
        i = -1
        curr_user_index = 0
        for user in users:
            try:
                music_profile = user.userprofile.interests.musicprofile
                i = i + 1
                data["myindex"].append(i)
                data["user_ID"].append(user.id)
                if(user.id == request.user.id):
                    curr_user_index = i
                genres = [x.strip() for x in music_profile.genres.split(',')]
                data["genres"].append(genres)
                popularities = [float(x) for x in music_profile.popularities.split(',')]
                data["popularity"].append(popularities)
                durations = [float(x) for x in music_profile.durations.split(',')]
                data["duration"].append(durations)
            except:
                pass
        if data["user_ID"]:
            df = pd.DataFrame(data)
            print(df.head())
            recommendations = generate_recommendations(df, curr_user_index)
            recommendations = [CustomUser.objects.get(pk=x) for x in recommendations]
            recommendations_final = []
            for recommendation in recommendations:
                if not request.user.userprofile.matches.filter(pk=recommendation.id).exists():
                    recommendations_final.append(recommendation)
            return render(request, 'dating/dashboard.html', context={'recommendations': recommendations_final, 'form': form})
    else:
        return render(request, 'dating/dashboard.html', context={'form': form})

def dashboard_like(request):
    liked_user = CustomUser.objects.get(pk=request.GET.get('param_first'))
    if request.user.userprofile.pending.filter(pk=liked_user.id).exists():
        request.user.userprofile.pending.remove(liked_user)
        request.user.userprofile.matches.add(liked_user)
        liked_user.userprofile.matches.add(request.user)
        thread = Thread.objects.create(first_person=request.user, second_person=liked_user)
    else:
        liked_user.userprofile.pending.add(request.user)

    response_data = 'successful!'

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )

def pending(request):
    pending_users = request.user.userprofile.pending.all()
    return render(request, 'dating/pending.html', context={'pending_users': pending_users})


def match_user(request):
    matched_user = CustomUser.objects.get(pk=request.GET.get('param_first'))
    request.user.userprofile.pending.remove(matched_user)
    matched_user.userprofile.matches.add(request.user)
    request.user.userprofile.matches.add(matched_user)

    response_data = 'successful!'

    thread = Thread.objects.create(first_person=request.user, second_person=matched_user)

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )

@login_required
def Interests(request):
    mylist = []
    try:
        if request.user.userprofile.interests.musicprofile:
            mylist.append("Music")
    except:
        pass
    try:
        if request.user.userprofile.interests.booksprofile:
            mylist.append("Books")
    except:
        pass
    try:
        if request.user.userprofile.interests.animeprofile:
            mylist.append("Anime")
    except:
        pass
    try:
        if request.user.userprofile.interests.moviesprofile:
            mylist.append("Movies")
    except:
        pass
    return render(request , 'dating/interests.html', context={"mylist": mylist})

def add_music(request):
    user_spotify_data = getUserSpotifyInfo()
    if(user_spotify_data == None):
        return redirect('dating-interests')
    
    user_music_profile = MusicProfile.objects.create(interests=request.user.userprofile.interests)
    user_music_profile.genres = ','.join(user_spotify_data['genres'])
    user_music_profile.artists = ','.join(user_spotify_data['artists'])
    user_music_profile.popularities = ','.join(map(str, user_spotify_data['popularities']))
    user_music_profile.durations = ','.join(map(str, user_spotify_data['durations']))
    user_music_profile.save()

    return redirect('dating-interests')

