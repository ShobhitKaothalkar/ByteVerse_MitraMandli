import base64
from requests import post
import json

client_id ="e8d096f73ead4c91a735c4da59ec6004"
client_secret ="5fb0e57bc4614bd9beb6876da905b319"
print(client_id , client_secret)


def get_token():
    auth_string = client_id+ ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes) , "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers ={
        "Authorization" : "Basic" + auth_base64,
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    data = {"grant_type" : "client_credentials"}
    result = post(url , headers = headers , data = data)
    json_result = json.loads(result.content)
    token = json_result
    #token = json_result["access_token"]
    return token

token = get_token()
print(token)


def get_auth_header(token):
    return {"Authorization" : "Bearer " + token}