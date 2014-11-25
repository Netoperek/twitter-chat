import urlparse
import requests
import json
import oauth2 as oauth
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from  main.twitter_data import TWITTER_AUTH, ATOKEN, CONSUMER_KEY, CONSUMER_SECRET, ASECRET
from django.contrib.auth.decorators import login_required

consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)

def create_friends_drict(friends_json):
    friends_dict = { }
    for user in friends_json['users']:
        user_id = user['id']
        user_name = user['name']
        friends_dict[user_id] = user_name
    return friends_dict

def get_users_dict(screen_name):
    url = 'https://api.twitter.com/1.1/friends/list.json?skip_statues=1&screen_name=' + screen_name
    req = requests.get(url, auth = TWITTER_AUTH)
    friends_json = json.loads(req.content)

    # Just for now
    #
    if req.status_code != 200:
      raise Exception("Twitter api did not return users list correctly")

    return create_friends_drict(friends_json)

