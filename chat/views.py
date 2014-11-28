from django.shortcuts import render, render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
import json
import requests
import oauth2 as oauth
from  main.twitter_data import CONSUMER_KEY, CONSUMER_SECRET

consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)

def create_friends_dict(friends_json):
    friends_dict = { }
    for user in friends_json['users']:
        user_id = user['id']
        user_name = user['name']
        friends_dict[user_id] = user_name
    return friends_dict

def get_users_dict(screen_name, access_token):
    url = 'https://api.twitter.com/1.1/friends/list.json?skip_statues=1&screen_name=' + screen_name
    token = oauth.Token(access_token['oauth_token'], access_token['oauth_token_secret'])
    oauth_request = oauth.Request.from_consumer_and_token(consumer, http_url = url)
    oauth_request.sign_request(oauth.SignatureMethod_HMAC_SHA1(), consumer, token)
    response = requests.get(url, headers = oauth_request.to_header())


    if response.status_code != 200:
      reason = str(response.content)
      raise Exception("Twitter api did not return users list correctly, reason: " + reason)

    friends_json = json.loads(response.content)

    return create_friends_dict(friends_json)


@login_required
def chat(request):
    access_token = request.session['token']
    screen_name = request.session['screen_name']
    friends_dict = get_users_dict(screen_name, access_token)
    print friends_dict

    return render_to_response("chat.html",
			        locals(),
			        context_instance=RequestContext(request))
