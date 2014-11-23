from django.shortcuts import render, render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
from  main.twitter_data import TWITTER_AUTH
import requests
import json

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
    return create_friends_drict(friends_json)

@login_required
def home(request):
    users = get_users_dict("PiotrKala")
    #users = { '1' : 'Piorek', '2' : 'Tomek', '3' : 'ktos' }
    return render_to_response("home.html",
                                locals(),
                                context_instance=RequestContext(request))
