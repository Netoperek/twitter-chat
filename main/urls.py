from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',

    # home
    #
    url(r'^$', 'home.views.home', name='home'),
    url(r'^home$', 'home.views.home', name='home'),

    # authentication
    #
    url(r'^login$', 'users.views.login_user', name='login'),
    url(r'^register$', 'users.views.register', name='register'),
    url(r'^invalidLogin$', 'users.views.invalidLogin', name='invalidLogin'),
    url(r'^logout$', 'users.views.logout_user', name='logout'),
)
