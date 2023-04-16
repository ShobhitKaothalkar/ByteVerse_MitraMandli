from django.shortcuts import render
#import spotipy
# Create your views here.
# def home(request):
#   from spotipy.oauth2 import SpotifyClientCredentials
#   cid = 'e8d096f73ead4c91a735c4da59ec6004'
#   secret = '5fb0e57bc4614bd9beb6876da905b319'
#   client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
#   sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#   artist_name = []
#   track_name = []
#   popularity = []
#   track_id = []
#   for i in range(0,10000,50):
#       track_results = sp.search(q='year:2018', type='track', limit=50,offset=i)
#       for i, t in enumerate(track_results['tracks']['items']):
#           artist_name.append(t['artists'][0]['name'])
#           track_name.append(t['name'])
#           track_id.append(t['id'])
#           popularity.append(t['popularity'])
#   print(artist_name)
#   return  render(request , 'spotify_test_app/home.html',{context : artist_name})



# BQBUgYH0g8lwYfPk8b4eL_l4hizAA8zf4Gp1hRp_7cQa7xvum_DymQ40V3Dqa2th-I4bXwrfBe3dzfk0OGN_aOIVfB_WkboK-IN-iU-dTlAAbjH2W3t74xfdmX0zcmomV11QWCwr-Q8MdTyZuNahP328FXubLIzui3U3KFKEBzDRVDFrJH39MvMzVQSGjV5nnWaqHgqb1gjxNkaShOP0K_Yl53jb5rVUbFYMmNGsV1qDqpOEEltmH_RoVdWdQEsvI0zzL7qF1xiYyTA
# AQAFqaDG-POgj90aIoNlUKG3h-3SbJGydhFfBoiKOJQUXHMrFWpNbNxaB5_cr3dIvV_lFG3r06wot8zQ0ukf_o8KPDiEjieyBlO0DMYNOaiZi-WdFkmJNqbSXIX9hWZryME
# client id : e8d096f73ead4c91a735c4da59ec6004
# client secret : 5fb0e57bc4614bd9beb6876da905b319



def home(request):
  return render(request , 'spotify_test_app/home.html')