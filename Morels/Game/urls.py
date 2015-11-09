from django.conf.urls import url

urlpatterns = [
    url(r'^(?P<game_id>\d+)/$', 'Game.views.game', name='game'),
    url(r'^(?P<game_id>\d+)/update/', 'Game.views.update', name='update'),
    url(r'^(?P<game_id>\d+)/checkval/', 'Game.views.cardClass', name='cardClass')
]
