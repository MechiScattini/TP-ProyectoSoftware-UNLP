from flask import redirect, request
import requests
from oauthlib.oauth2 import WebApplicationClient
import json

# Configuration
GOOGLE_CLIENT_ID = '44050287165-rcvai5a3fmnmgv7tuu1ok4kegj62ut1e.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = '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'
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()

client = WebApplicationClient(GOOGLE_CLIENT_ID)

def login_with_google():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri="https://admin-grupo18.proyecto2021.linti.unlp.edu.ar/login/callback-google",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)
    
def callback_google():
    # Get authorization code Google sent back to you
    code = request.args.get("code")

    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))
    
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    return userinfo_response