from django.shortcuts import render, render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
import json
import requests
import oauth2 as oauth
from  main.twitter_data import CONSUMER_KEY, CONSUMER_SECRET

consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
chat_dict_g = { }
chat_dict = chat_dict_g

def create_friends_dict(friends_json):
    friends_dict = { }
    for user in friends_json['users']:
        user_id = user['id']
        user_name = user['name']
        friends_dict[user_id] = user_name
    return friends_dict

def get_users_dict(screen_name, access_token):
    url = 'https://api.twitter.com/1.1/followers/list.json?skip_statues=1&screen_name=' + screen_name
    token = oauth.Token(access_token['oauth_token'], access_token['oauth_token_secret'])
    oauth_request = oauth.Request.from_consumer_and_token(consumer, http_url = url)
    oauth_request.sign_request(oauth.SignatureMethod_HMAC_SHA1(), consumer, token)
    response = requests.get(url, headers = oauth_request.to_header())

    if response.status_code != 200:
      reason = str(response.content)
      raise Exception("Twitter api did not return users list correctly, reason: " + reason)

    friends_json = json.loads(response.content)

    return create_friends_dict(friends_json)

def send_chat_request(screen_name, access_token):
    url = 'https://api.twitter.com/1.1/account/settings?lang=en'
    token = oauth.Token(access_token['oauth_token'], access_token['oauth_token_secret'])
    oauth_request = oauth.Request.from_consumer_and_token(consumer, http_url = url)
    oauth_request.sign_request(oauth.SignatureMethod_HMAC_SHA1(), consumer, token)
    response = requests.post(url, headers = oauth_request.to_header())

    if response.status_code != 200:
      reason = str(response.content)
      raise Exception("Direct message not send, reason: " + reason + " " + str(response.status_code))

def invate_selected_users(access_token):
    print chat_dict_g.values()
    for value in chat_dict_g.values():
        send_chat_request(value, access_token)

@login_required
def chat(request):
    show = False
    access_token = request.session['token']
    screen_name = request.session['screen_name']
    friends_dict = get_users_dict(screen_name, access_token)

    current_msg = ""
    chat_dict = chat_dict_g

    if request.POST.get("add_to_chat", ""):
        receiver_id = request.POST['id']
        receiver_name = friends_dict.get(int(receiver_id))
        if receiver_id in chat_dict:
            chat_dict_g.pop(receiver_id, 0)
        else:
            chat_dict_g[receiver_id] = receiver_name

    if request.POST.get("create_chat", ""):
        show = True
        invate_selected_users(access_token)

    if request.POST.get("send", ""):
        show = True
        msg = request.POST['msg']
        receiver_id = request.POST['id']

    return render_to_response("chat.html",
			        locals(),
			        context_instance=RequestContext(request))
