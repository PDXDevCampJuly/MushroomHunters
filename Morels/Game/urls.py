from django.conf.urls import url

urlpatterns = [
    url(r'^(?P<game_id>\d+)/$', 'Game.views.game', name='game')
]
