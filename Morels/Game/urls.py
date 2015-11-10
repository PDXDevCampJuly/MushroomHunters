from django.conf.urls import url

urlpatterns = [
    url(r'^(?P<game_id>\d+)/$', 'Game.views.game', name='game'),
    url(r'^(?P<game_id>\d+)/update/', 'Game.views.update', name='update'),
    url(r'^(?P<game_id>\d+)/sell_cards/', 'Game.views.sell_cards', name='sell_cards'),
    url(r'^(?P<game_id>\d+)/play_cards/', 'Game.views.play_cards', name='play_cards'),
    url(r'^(?P<game_id>\d+)/buy_cards/', 'Game.views.buy_cards', name='play_cards'),
]
