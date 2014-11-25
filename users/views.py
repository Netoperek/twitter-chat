from django.shortcuts import render, render_to_response, RequestContext
from requests_oauthlib import OAuth1
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.models import Chat_user
from  main.twitter_data import TWITTER_AUTH, ATOKEN, CONSUMER_KEY, CONSUMER_SECRET, ASECRET
import requests
import oauth2 as oauth
import urlparse

consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
client = oauth.Client(consumer)
client.add_certificate

request_token_url = 'https://api.twitter.com/oauth/request_token'
authorize_url = 'https://api.twitter.com/oauth/authorize'
callback_url = 'https://127.0.0.1:8000/'

def sign_in_by_twitter(request):
    oauth_request = oauth.Request.from_consumer_and_token(
            consumer, \
            http_url=request_token_url, \
            parameters = {'oauth_callback':callback_url})

    oauth_request.sign_request(oauth.SignatureMethod_HMAC_SHA1(), consumer, None)
    response = requests.get(request_token_url, headers=oauth_request.to_header(), verify=True)
    request_token = dict(urlparse.parse_qsl(response.content))
    request.session['auth'] = request_token

    url = 'https://api.twitter.com/oauth/authorize?oauth_token=%s' % request_token['oauth_token']
    return HttpResponseRedirect(url)

def login_user(request):
    return sign_in_by_twitter(request)

def invalidLogin(request):
    return render_to_response("invalidLogin.html",
			        locals(),
			        context_instance=RequestContext(request))
@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect("home")
