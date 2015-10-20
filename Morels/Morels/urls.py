"""Morels URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from Player import views
import Game
from Game import urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'Player.views.signup', name='signup'),
    url(r'^login/', 'Player.views.log_in', name='login'),
    url(r'^home/', 'Player.views.home', name='home'),
    url(r'^logout/$', 'Player.views.user_logout', name='logout'),
    url(r'^profile/', 'Player.views.profile', name='profile'),
    url(r'^invite/', 'Game.views.invite', name='invite'),
    url(r'^game/', 'Game.views.game', name='make_starting_deck'),
    url(r'^newgame/', 'Game.views.new_game', name='newgame'),
    url(r'^leader_board/', 'Player.views.leader_board', name='leader_board'),
    # url(r'^game/$', include(Game.urls)),
    # url(r'^game/', include('Game.urls', namespace="game_urls")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                             document_root=settings.MEDIA_ROOT)
