from django.shortcuts import render, render_to_response, RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.models import Chat_user
from  main.twitter_data import TWITTER_AUTH
import requests

def register_page(request):
  form = UserCreationForm(request.POST)
  return render_to_response("register.html",
                              locals(),
                              context_instance=RequestContext(request))

def check_twitter_account():
    url = 'https://api.twitter.com/oauth/request_token'
    req = requests.post(url, auth = TWITTER_AUTH)
    print "HERE " + str(req.content)

def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      new_user = form.save()
      user = Chat_user(user = new_user)
      user.save()
      return HttpResponseRedirect('home')
    else:
      return register_page(request)
  else:
    return register_page(request)

#TODO login with twitter
def login_user(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        #check_twitter_account()
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                return HttpResponse("Your Django account is disabled.")
        else:
            return HttpResponseRedirect("invalidLogin")
    else:
        return render_to_response("login.html",
                                    locals(),
                                    context_instance=RequestContext(request))

def invalidLogin(request):
    return render_to_response("invalidLogin.html",
			        locals(),
			        context_instance=RequestContext(request))

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect("home")
