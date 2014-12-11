import time
import tweepy
import json
import requests
import oauth2 as oauth
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.shortcuts import render, render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
from main.twitter_data import CONSUMER_KEY, CONSUMER_SECRET
from chat.models import ChatRoom
from chat.models import Message
from django.contrib.auth.models import User
from users.models import Chat_user

def get_friends_dict(screen_name, api):
    users = {}
    for user in tweepy.Cursor(api.followers, screen_name = screen_name).items():
        users[user.id_str] = user.screen_name
    return users

def chat_name_unique(chat_name):
    chat_name = ChatRoom.objects.filter(name = chat_name)
    if chat_name:
        return False
    else:
        return True

def get_chat_user(screen_name):
    user = User.objects.filter(username = screen_name)
    chat_user = Chat_user.objects.get(user = user)
    return chat_user

def close_chat(request, user):
    user.chat_name = 'null'
    user.chat_not_created = True
    user.show_chat_panel = False
    user.save()

def create_chat(request, user):
    chat_name = request.POST.get('chat_name', '')
    if len(chat_name.strip()) == 0:
        user.show_wrong_chat_name_msg = True
        user.save()
    elif chat_name_unique(chat_name):
        user.chat_name = chat_name
        user.show_chat_panel = True
        user.chat_not_created = False
        user.save()
        chat = ChatRoom(name = chat_name)
        chat.save()
    else:
        user.show_wrong_chat_name_msg = True
        user.save()

def go_to_room(request, user):
    chat_name = request.POST.get('name', '')
    user.chat_name = chat_name 
    user.show_chat_panel = True
    user.chat_not_created = False
    user.save()

def send(request, user):
    text = request.POST.get('msg', '')
    chat_room = ChatRoom.objects.get(name = user.chat_name)
    msg = Message(room = chat_room, content = text, author = user.user.username)
    msg.save()

@login_required
def chat(request):
    screen_name = request.session['screen_name']
    user = get_chat_user(screen_name)

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(request.session['twitter_access_token_key'], request.session['twitter_access_token_secret'])
    api = tweepy.API(auth_handler=auth)

    friends_dict = get_friends_dict(screen_name, api)

    if Chat_user.objects.count() != 0:
        in_chat = Chat_user.objects.filter(chat_name = user.chat_name) 
        rooms = ChatRoom.objects.all()
        messages = Message.objects.filter(room = in_chat)

    if 'close_chat' in request.POST:
        close_chat(request, user)

    if 'create_chat' in request.POST:
        create_chat(request, user)

    if 'go_to_room' in request.POST:
        go_to_room(request, user)

    if 'send' in request.POST:
        send(request, user)

    return render_to_response("chat.html",
                                locals(),
                                context_instance=RequestContext(request))
