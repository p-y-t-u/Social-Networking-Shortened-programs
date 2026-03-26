import requests
from requests_oauthlib import OAuth1

def get_user(k, ks, t, ts):
    r = requests.get(
        "https://api.twitter.com/2/users/me",
        auth=OAuth1(k, ks, t, ts)
    )
    if r.status_code == 200:
        d = r.json()["data"]
        print("User ID:", d["id"])
        print("Username:", d["username"])
    else:
        print("Error:", r.status_code, r.text)

# credentials
api_key = "LMwvRn4KV2qWwNI7ZhyWLNIhw"
api_secret_key = "nB324r6e4Rz19LsFJPbBYnCEwWw8VcLatTlAtV05v7K7oQykrP"
access_token = "2008441416264151040-WQ4bgM1DzpcYKWO5SsTzsFr33gAZ55"
access_token_secret = "cIIEQkRSIq8rcOyt782yBnwY22tJqCw7TECAaGMPjcWSF"

get_user(api_key, api_secret_key, access_token, access_token_secret)
