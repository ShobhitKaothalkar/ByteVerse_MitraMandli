import json
import requests
import secrets
import webbrowser

CLIENT_ID = 'f945d7120fb23292c601f8b65b2fefa9'
CLIENT_SECRET = 'e5fea099b6355cc719ec4b118aab51352918e4c7f0f02fe68363b160873b3760'
anime_id = []
anime_title =[]
anime_genres =[]
anime_mean=[]
anime_popularity = []


# 1. Generate a new Code Verifier / Code Challenge.
def get_new_code_verifier() -> str:
    token = secrets.token_urlsafe(100)
    return token[:128]


# 2. Print the URL needed to authorise your application.
def print_new_authorisation_url(code_challenge: str):
    global CLIENT_ID

    url = f'https://myanimelist.net/v1/oauth2/authorize?response_type=code&client_id={CLIENT_ID}&code_challenge={code_challenge}'
    print(f'Authorise your application by clicking here: {url}\n')
    # url = f'https://myanimelist.net/v1/oauth2/authorize?response_type=code&client_id={CLIENT_ID}&code_challenge={code_challenge}'
    # webbrowser.open(url)



# 3. Once you've authorised your application, you will be redirected to the webpage you've
#    specified in the API panel. The URL will contain a parameter named "code" (the Authorisation
#    Code). You need to feed that code to the application.
def generate_new_token(authorisation_code: str, code_verifier: str) -> dict:
    global CLIENT_ID, CLIENT_SECRET

    url = 'https://myanimelist.net/v1/oauth2/token'
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': authorisation_code,
        'code_verifier': code_verifier,
        'grant_type': 'authorization_code'
    }

    response = requests.post(url, data)
    response.raise_for_status()  # Check whether the request contains errors

    token = response.json()
    response.close()
    print('Token generated successfully!')

    with open('token.json', 'w') as file:
        json.dump(token, file, indent = 4)
        print('Token saved in "token.json"')
        # print(token)

    return token


# 4. Test the API by requesting your profile information
def print_user_info(access_token: str):
    url = 'https://api.myanimelist.net/v2/users/@me'
    response = requests.get(url, headers = {
        'Authorization': f'Bearer {access_token}'
        })
    
    response.raise_for_status()
    user = response.json()
    response.close()


    url1 = f"https://api.myanimelist.net/v2/users/{user['name']}/animelist"
    response1 = requests.get(url1, headers = {
        'Authorization': f'Bearer {access_token}'
        })
    response1.raise_for_status()
    list = response1.json()
    my_list = json.dumps(list, indent = 4) 
    response1.close()

    for node in list['data']:
        # print(node['node'])
        # print(type(node))
        anime_id.append(node['node']['id'])
        anime_title.append(node['node']['title'])
    cntr = 0
    for id in anime_id:
        if cntr>=10:
            break
        url2 = f"https://api.myanimelist.net/v2/anime/{id}?fields=mean,rank,popularity,genres"
        response2 = requests.get(url2, headers = {
            'Authorization': f'Bearer {access_token}'
        })
        response2.raise_for_status()
        details = response2.json()
        anime_mean.append(details['mean'])
        anime_popularity.append(details['popularity'])
        genres = details['genres']
        for genre in genres:
            anime_genres.append(genre['name'])
        # details_json  = json.dumps(details, indent = 4) 
        # anime_genres.append(genre)
        response2.close()

    
    print(f"\n>>> Greetings {user['name']}! <<<")
    print(f"\n anime means:>>> {anime_mean}")
    print(f"\n anime popularity:>>> {anime_popularity}")
    print(f"\n anime genres:>>> {anime_genres}")
    # anime_data_list  =[("means" , anime_mean) , ("popularity" , anime_popularity , ("genres" , genres))]
    # anime_data = dict(anime_data_list)
    # return anime_data
    # print(f"\n anime details>>> {details_json}")


if __name__ == '__main__':
    code_verifier = code_challenge = get_new_code_verifier()
    print_new_authorisation_url(code_challenge)

    authorisation_code = input('Copy-paste the Authorisation Code: ').strip()
    token = generate_new_token(authorisation_code, code_verifier)

    print_user_info(token['access_token'])


#http://localhost:8000/interests/add-anime





