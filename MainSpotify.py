from spotify_secrets import token
import json
import requests
api_url = 'https://api.spotify.com/v1/'

def get_profile():
    user_id = input('What is your Spotify User ID?: ')
    profile_request = '{}{}'.format(api_url, user_id)
    response = requests.get(
        profile_request,
        headers = {
            "Accept: application/json",
            "Content-Type: application/json",
            "Bearer {}".format(token)
        }
    )
    response_json = response.json()
    print(reponse_json)


get_profile()
