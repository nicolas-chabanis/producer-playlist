import json
import requests
from flask import Flask, request, render_template, redirect, url_for
from urllib.parse import quote

import api_key

app = Flask(__name__)

# Spotify URLS
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)

# Server-side Parameters
CLIENT_SIDE_URL = "http://127.0.0.1"
PORT = 8080
REDIRECT_URI = "{}:{}/callback/q".format(CLIENT_SIDE_URL, PORT)
SCOPE = "playlist-modify-public playlist-modify-private"
STATE = ""
SHOW_DIALOG_bool = True
SHOW_DIALOG_str = str(SHOW_DIALOG_bool).lower()

auth_query_parameters = {
    "response_type": "code",
    "redirect_uri": REDIRECT_URI,
    "scope": SCOPE,
    # "state": STATE,
    # "show_dialog": SHOW_DIALOG_str,
    "client_id": api_key.SPOTIFY_CLIENT_ID
}

@app.route('/')
def index():
    return render_template("index.html", title="Home")

@app.route('/login', methods=['GET', 'POST'])
def login():
    url_args = "&".join(["{}={}".format(key, quote(val)) for key, val in auth_query_parameters.items()])
    auth_url = "{}/?{}".format(SPOTIFY_AUTH_URL, url_args)
    return redirect(auth_url)

@app.route('/test')
def test():
    return "Hello World"

@app.route("/callback/q")
def callback():
    # # Auth Step 4: Requests refresh and access tokens
    # auth_token = request.args['code']
    # code_payload = {
    #     "grant_type": "authorization_code",
    #     "code": str(auth_token),
    #     "redirect_uri": REDIRECT_URI,
    #     'client_id': api_key.SPOTIFY_CLIENT_ID,
    #     'client_secret': api_key.SPOTIFY_CLIENT_SECRET,
    # }
    # post_request = requests.post(SPOTIFY_TOKEN_URL, data=code_payload)

    # # Auth Step 5: Tokens are Returned to Application
    # response_data = json.loads(post_request.text)
    # access_token = response_data["access_token"]
    # refresh_token = response_data["refresh_token"]
    # token_type = response_data["token_type"]
    # expires_in = response_data["expires_in"]

    # # Auth Step 6: Use the access token to access Spotify API
    # authorization_header = {"Authorization": "Bearer {}".format(access_token)}

    # # Get profile data
    # user_profile_api_endpoint = "{}/me".format(SPOTIFY_API_URL)
    # profile_response = requests.get(user_profile_api_endpoint, headers=authorization_header)
    # profile_data = json.loads(profile_response.text)

    return render_template("index.html")
