from django.shortcuts import render, render_to_response, RequestContext
import urlparse
from  main.twitter_data import TWITTER_AUTH, ATOKEN, CONSUMER_KEY, CONSUMER_SECRET, ASECRET
from django.contrib.auth.decorators import login_required
import requests
import json
import oauth2 as oauth

consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)

def create_friends_drict(friends_json):
    friends_dict = { }
    for user in friends_json['users']:
        user_id = user['id']
        user_name = user['name']
        friends_dict[user_id] = user_name
    return friends_dict

def get_users_dict(screen_name):
    #url = 'https://api.twitter.com/1.1/friends/list.json?skip_statues=1&screen_name=' + screen_name
    #friends_json = json.loads(req.content)

    # Just for now
    #
    if req.status_code != 200:
      raise Exception("Twitter api did not return users list correctly")

    print req.content

    #return create_friends_drict(friends_json)

def home(request):
    url = 'https://api.twitter.com/1.1/account/verify_credentials.json'

    oauth_token = request.GET.get("oauth_token", "") 
    oauth_verifier = request.GET.get("oauth_verifier","") 
    access_token_url = 'https://api.twitter.com/oauth/access_token?oauth_verifier=' + oauth_verifier
    access_token = request.session['auth']

    token = oauth.Token(oauth_token, access_token['oauth_token_secret'])
    oauth_request = oauth.Request.from_consumer_and_token(consumer, http_url=access_token_url)
    oauth_request.sign_request(oauth.SignatureMethod_HMAC_SHA1(), consumer, token)

    response = requests.post(access_token_url, headers=oauth_request.to_header())
    access_token = dict(urlparse.parse_qsl(response.content))

    token = oauth.Token(access_token['oauth_token'], access_token['oauth_token_secret'])
    oauth_request = oauth.Request.from_consumer_and_token(consumer, http_url=url)
    oauth_request.sign_request(oauth.SignatureMethod_HMAC_SHA1(), consumer, token)

    # get the resource
    response = requests.get(url, headers=oauth_request.to_header())

    print "HERE " + str(response.status_code)
    print "HERE1 " + str(response.content)
    #users = get_users_dict("PiotrKala")

    # If twitter api requests are more then 100
    #
    users = { '1' : 'Piorek', '2' : 'Tomek', '3' : 'ktos' }
    return render_to_response("home.html",
                                locals(),
                                context_instance=RequestContext(request))
