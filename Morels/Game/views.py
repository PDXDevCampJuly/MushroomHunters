from django.shortcuts import render
from .models import *
from random import shuffle
# from random import choice
from Game.models import Forest, Night, Deck, Decay
# from django.contrib.auth.models import User
from Player.models import Card, User, Player, MyUser
from django.shortcuts import redirect
# import random


def make_starting_decks(person, person1):
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

            forest.forestCard.add(c)

            forest.save()

            num += 1

        if num < 11:
            person.userHand.add(c)
            person.save()
            num +=1
        if num > 11 and num < 16:
            person1.userHand.add(c)
            person1.save()
            num +=1
        else:
            deck.deckCard.add(c)
            deck.save()
            num += 1

    decay = Decay()
    decay.save()

    for n in Card.objects.filter(type__startswith='Night'):
        night.nightDeckCard.add(n)
        night.save()


def invite(request):
    me = request.user
    people = User.objects.all().exclude(username=me.username)

    return render(request, 'invite.html', {'people': people, 'me': me})


def new_game(request):

    if request.method == 'POST':
        player2 = request.POST.get("player2")

        user_object = User.objects.filter(username__exact=player2)

        real_user = MyUser.objects.get(user=user_object)

        person = Player(userPlayer=real_user)
        person.save()

        player1 = request.user

        real_user1 = MyUser.objects.get(user__exact=player1)

        person1 = Player(userPlayer=real_user1)
        person1.save()

        make_starting_decks(person, person1)

        create_game(person, person1)

        return redirect('/game/')

    else:
        return redirect('/invite/')


def create_game(person, person1):
    deck = Deck.objects.all()[:1].get()
    forest = Forest.objects.all()[:1].get()
    night = Night.objects.all()[:1].get()
    decay = Decay.objects.all()[:1].get()

    game=Game(player_1=person, player_2=person1, deck_id=deck, forest_id=forest, night_id=night, decay_id=decay,)
    game.save()


def game(request):
    player_hand = request.user

    user = MyUser.objects.get(user__exact=player_hand)

    boop = Player.objects.filter(userPlayer=user)

    blah = boop.all()[:1].get()

    hand = blah.userHand.all()



    return render(request, 'game.html', {'hand' : hand})