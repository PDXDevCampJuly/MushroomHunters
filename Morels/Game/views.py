from django.shortcuts import render
from .models import *
from random import shuffle
from random import choice
from Game.models import *
from django.contrib.auth.models import User
import random


def make_starting_decks(request):
    card =[]
    forest = Forest()
    forest.save()
    night = Night()
    night.save()
    deck = Deck()
    deck.save()

    for i in Card.objects.filter().exclude(type__startswith='Night'):
        card.append(i)
    shuffle(card)
    print(card)

    e = 0
    for c in card:
        if e < 3:
            forest.forestCard.add(c)
            forest.save()
            print(forest)
            e += 1
        else:
            deck.deckCard.add(c)
            e += 1
            print(deck)

    decay = Decay()
    decay.save()

    for n in Card.objects.filter(type__startswith='Night'):
        night.nightDeckCard.add(n)
        night.save()
        print(night)

    return render(request, 'game.html', {'decay': decay, 'forest': forest,})


def invite(request):
    me = request.user
    people = User.objects.all().exclude(username = me.username)

    return render(request, 'invite.html', {'people': people, 'me': me})

def new_game(request):

    if request.method == 'POST':
        player2 = request.POST.get("player2")
        user2 = User.objects.all().filter(username=player2)
        user1 = request.user
        create_game(user1, user2)

    return render(request, 'game.html')


def create_game(user1, user2):
    deck = Deck.objects.all()
    forest = Forest.objects.all()
    night = Night.objects.all()
    decay = Decay.objects.all()

    game=Game(player_1=user1, player_2=user2[0], deck_id=deck[0], forest_id=forest[0], night_id=night[0], decay_id=decay[0],)
    game.save()
