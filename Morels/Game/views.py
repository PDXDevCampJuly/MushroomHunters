from django.shortcuts import render
from .models import *
from random import shuffle
from random import choice
from Game.models import Forest, Night, Deck, Decay
from django.contrib.auth.models import User
from Player.models import Card, User, Player, MyUser
import random


def make_starting_decks(request):
    cards = []
    forest = Forest()
    forest.save()
    night = Night()
    night.save()
    deck = Deck()
    deck.save()

    for i in Card.objects.filter().exclude(type__startswith='Night'):
        cards.append(i)
    shuffle(cards)

    num = 0
    for c in cards:

        if num < 8:

            forest.forestCard.add(c.id)

            forest.save()

            num += 1

        else:
            deck.deckCard.add(c)
            deck.save()
            num += 1

    decay = Decay()
    decay.save()

    for n in Card.objects.filter(type__startswith='Night'):
        night.nightDeckCard.add(n)
        night.save()
        # print(night)

    return render(request, 'game.html', {'decay': decay, 'forest': forest,})


def invite(request):
    me = request.user
    people = User.objects.all().exclude(username=me.username)

    return render(request, 'invite.html', {'people': people, 'me': me})


def new_game(request):

    if request.method == 'POST':
        player2 = request.POST.get("player2")

        user_object = User.objects.filter(username__exact=player2) #User object
        print(user_object)
        print('user_object')

        real_user = MyUser.objects.get(user=user_object)
        print(real_user)
        print('real_user')

        person = Player(userPlayer=real_user)
        person.save()

        player1 = request.user
        print(player1)
        print('player1')

        real_user1 = MyUser.objects.get(user__exact=player1)
        print(real_user1)
        print('real_user1')

        person1 = Player(userPlayer=real_user1)
        person1.save()

        create_game(person, person1)

    return render(request, 'game.html')


def create_game(person, person1):
    deck = Deck.objects.all()[:1].get()
    forest = Forest.objects.all()[:1].get()
    night = Night.objects.all()[:1].get()
    decay = Decay.objects.all()[:1].get()

    game=Game(player_1=person, player_2=person1, deck_id=deck, forest_id=forest, night_id=night, decay_id=decay,)
    game.save()



# if num < 11:
#     player.userHand.add(c)
#     player.save()
#     print('Printing Hand')
#     print(player)