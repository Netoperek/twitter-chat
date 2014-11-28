from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',

    # home
    #
    url(r'^$', 'users.views.home', name='home'),
    url(r'^home$', 'users.views.home', name='home'),

    # authentication
    #
    url(r'^login$', 'users.views.login_user', name='login'),

    # chat page
    #
    url(r'^chat$', 'chat.views.chat', name='chat'),
)
