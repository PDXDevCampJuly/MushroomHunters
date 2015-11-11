# IMPORTS
from .models import *
from random import shuffle
from random import choice
from Game.models import Forest, Night, Deck, Decay
from Player.models import Card, User, Player, MyUser
from django.shortcuts import redirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
# END OF IMPORTS

def make_starting_decks(person, person1):
    """Appending cards into decks"""

    # Variables
    cards = []
    forest = Forest()
    forest.save()
    night = Night()
    night.save()
    deck = Deck()
    deck.save()

    for i in Card.objects.filter().exclude(type__startswith='Night'):
        #Appending all cards(except for the ones that's type is "Night") to the list cards
        cards.append(i)
    shuffle(cards)

    num = 0
    for c in cards:
        # Appending all cards from list cards into forest, userHand, and deck
        if num < 8:
            forest.forestCard.add(c)
            forest.save()
        if num > 7 and num < 11:
            person.userHand.add(c)
            person.save()
        if num > 12 and num < 16:
            person1.userHand.add(c)
            person1.save()
        else:
            deck.deckCard.add(c)
            deck.save()
        num += 1

    decay = Decay()
    decay.save()

    for n in Card.objects.filter(type__startswith='Night'):
        # Appending all cards with type "Night" into nightDeck
        night.nightDeckCard.add(n)
        night.save()

    list_of_decks = [forest.id, night.id, deck.id, decay.id]

    return list_of_decks

def invite(request):
    """Get's all player objects except current user"""
    me = request.user
    people = User.objects.all().exclude(username=me.username)

    return render(request, 'invite.html', {'people': people, 'me': me})


def new_game(request):
    """ Creates new Player objects with the given user and current user """

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

        test = make_starting_decks(person, person1)

        game_id = create_game(person, person1, test)
        return HttpResponseRedirect(reverse('game_urls:game', kwargs={'game_id': game_id}))

    else:
        return redirect('/invite/')


def create_game(person, person1, test):
    """ Creates new game with the right decks and users """
    deck = Deck.objects.get(id=test[0])
    forest = Forest.objects.get(id=test[1])
    night = Night.objects.get(id=test[2])
    decay = Decay.objects.get(id=test[3])

    players= []

    players.append(person1)
    players.append(person)

    game = Game(player_1=person,
                player_2=person1,
                current_player=choice(players),
                deck_id=deck,
                forest_id=forest,
                night_id=night,
                decay_id=decay,)
    game.save()

    return game.id


def game(request, game_id):
    """Prints game and calls all other functions (So this is basically main)"""

    game = Game.objects.get(pk=game_id)
    game_player = game.player_1
    player_sticks = 0
    hand = []
    forest = []
    playing = []
    decay = []
    player_one = Player.objects.get(id=game_player.id)
    player_two = Player.objects.get(id=game.player_2.id)
    current_player = game.current_player

    # Appending information to lists so I can send it to template
    if game_player.userPlayer.user.id == request.user.id:
        player_sticks = (player_one.sticks)
        for i in game.player_1.userHand.filter():
            hand.append(i)
        for crd in game.player_1.userPlayingCards.filter():
            playing.append(crd)

    elif game.player_2.userPlayer.user.id == request.user.id:
        player_sticks = player_two.sticks
        for i in game.player_2.userHand.filter():
            hand.append(i)
        for crd in game.player_2.userPlayingCards.filter():
            playing.append(crd)
    else:
        return redirect('/home/')

    user = request.user.username

    for mushroom in game.forest_id.forestCard.filter():
        forest.append(mushroom)

    for token in game.decay_id.decayDeckCard.filter():
        decay.append(token)

    test = json.dumps(game_player.userPlayer.user.username)

    boop = json.dumps(request.user.username)

    # Takes away turn from player and adds winner to game
    if game.current_player.turns >= 1:
        update(request, game_id)
        sell_cards(request, game_id)
        play_cards(request, game_id)
    else:
        if game.player_2.score >= game.player_1.score:


            game.winner = game.player_2.userPlayer
            game.winner.save()
        elif game.player_1.score >= game.player_2.score:
            game.winner = game.player_1.userPlayer
            game.winner.save()



    return render(request, 'game.html', {'hand': hand,
                                         'decay': decay,
                                         'forest': forest,
                                         'game_player': game_player,
                                         'test': test,
                                         'boop': boop,
                                         'game_id': game_id,
                                         'player_sticks': player_sticks,
                                         'current_player': current_player,
                                         'user': user,
                                         'playing': playing
                                         })


@csrf_exempt
def update(request, game_id):
    """Updates userHand and Forest"""

    if request.method == 'POST':
        post_forest = request.POST.getlist('forest[]')
        post_decay = request.POST.getlist('decay[]')
        game = Game.objects.get(id=game_id)
        forest_obj = game.forest_id
        decay_id = game.decay_id
        decay_obj = Decay.objects.get(id=decay_id.id)
        fore = Forest.objects.get(id=forest_obj.id)

        # Calling functions
        forest_card(game, post_forest, fore, request)
        decay_card(game, post_decay, decay_obj, request)

        # Changing decay and forest
        decay = game.forest_id.forestCard.get(id=post_forest[1])
        other_decay = Card.objects.get(id=decay.id)

        decay_obj.decayDeckCard.add(other_decay)
        decay_obj.save()

        fore.forestCard.remove(decay)
        fore.save()

        # Calls function to change player
        update_player(game)

        try:
            print("Yoo")
        except:
            print('no good')

        return HttpResponse(
            print("blah")
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"})
        )


def forest_card(game, post_forest, fore, request):
    """Updates forest"""
    post_test = request.POST.getlist('testest[]')
    forest = game.forest_id.forestCard.all()
    forest_cards = []
    num = len(post_forest) - 1
    deck = game.deck_id
    forest_num = len(post_forest)

    # See's if player called this
    if len(post_test) >= 0:
        for i in forest:
            forest_cards.append(i.id)

        # Appends to cards_in_forest

        cards_in_forest = [str(i) for i in forest_cards]

        # Finds missing index in when comparing cards_in forest and post_forest
        missing_card = list(set(cards_in_forest) - set(post_forest))

        # Sorting list
        cards_in_forest.sort()
        post_forest.sort()

        # Loops through missing_card and appends cards to forest
        if forest_num != len(forest_cards):
            for i in missing_card:
                forest_delcard = game.forest_id.forestCard.filter(id=i)
                other_card = Card.objects.get(id=i)
                for e in forest_delcard:

                    if game.player_1.userPlayer.user.id == request.user.id:
                        fu = Player.objects.get(id=game.player_1.id)
                        fu.userHand.add(other_card)
                        fu.save()
                    elif game.player_2.userPlayer.user.id == request.user.id:
                        meanie = Player.objects.get(id=game.player_2.id)
                        meanie.userHand.add(other_card)
                        meanie.save()
                    fore.forestCard.remove(e)
                    fore.save()
        # Adds cards to forest until forest length is 8
        while num <= 8:
            fore.forestCard.add(deck.deckCard.order_by('?').first())
            fore.save()
            num += 1


def decay_card(game, post_decay, decay_obj, request):
    """Updates decay Basically the forest_card but with decay"""
    decay = game.decay_id.decayDeckCard.all()
    decay_cards = []

    decay_num = len(post_decay)

    for i in decay:
        decay_cards.append(i.id)

    cards_in_decay = []

    for i in decay_cards:
        cards_in_decay.append(str(i))


    missing = list(set(cards_in_decay) - set(post_decay))

    if decay_num == 4:
        decay_obj.decayDeckCard.clear()
        decay_obj.save()

    if decay_num != len(decay_cards):
        for i in missing:
            decay_delcard = game.decay_id.decayDeckCard.filter(id=i)
            other_card = Card.objects.get(id=i)

            for e in decay_delcard:
                if game.player_1.userPlayer.user.id == request.user.id:
                    player_one = Player.objects.get(id=game.player_1.id)
                    player_one.userHand.add(other_card)
                    player_one.save()
                elif game.player_2.userPlayer.user.id == request.user.id:
                    player_two = Player.objects.get(id=game.player_2.id)
                    player_two.userHand.add(other_card)
                    player_two.save()
                decay_obj.decayDeckCard.remove(e)
                decay_obj.save()



@csrf_exempt
def sell_cards(request, game_id):
    """Updates users hand and score"""
    if request.method == 'POST':
        post_check = request.POST.getlist('sellingCards[]')
        game = Game.objects.get(id=game_id)
        hand =[]
        sell_num = len(post_check)
        game_player = game.player_1

        if game_player.userPlayer.user.id == request.user.id:
            for i in game_player.userHand.all():
                hand.append(i.id)

        elif game.player_2.userPlayer.user.id == request.user.id:
            for i in game.player_2.userHand.all():
                hand.append(i.id)

        missing_card = list(set(post_check) - set(hand))

        for i in missing_card:
            if game_player.userPlayer.user.id == request.user.id:
                sel_crd = game.player_1.userHand.filter(id=i)
            elif game.player_2.userPlayer.user.id == request.user.id:
                sel_crd = game.player_2.userHand.filter(id=i)
            other_card = Card.objects.get(id=i)
            for e in sel_crd:

                if game.player_1.userPlayer.user.id == request.user.id:

                    game.player_1.userHand.remove(e)

                    game.player_1.userPlayingCards.add(other_card)

                    game.player_1.score += e.cardValue

                    game.player_1.save()

                elif game.player_2.userPlayer.user.id == request.user.id:
                    game.player_2.userHand.remove(e)

                    game.player_2.userPlayingCards.add(other_card)

                    game.player_2.score += e.cardValue

                    game.player_2.save()

        update_player(game)

        try:
            print("Yoo")
        except:
            print('no good')

        return HttpResponse(
            print("blah")
            )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
            )


@csrf_exempt
def play_cards(request, game_id):
    """Update userHand sticks"""
    # TODO: swap play_cards with sell_cards
    if request.method == 'POST':
        post_check = request.POST.getlist('sellingCards[]')
        game = Game.objects.get(id=game_id)
        hand =[]
        sell_num = len(post_check)
        game_player = game.player_1

        if len(post_check) >= 0:
            if game_player.userPlayer.user.id == request.user.id:
                for i in game_player.userHand.all():
                     hand.append(i.id)

            elif game.player_2.userPlayer.user.id == request.user.id:
                for i in game.player_2.userHand.all():
                     hand.append(i.id)


            missing_card = list(set(post_check) - set(hand))

            for i in missing_card:
                if game_player.userPlayer.user.id == request.user.id:
                    sel_card = game.player_1.userHand.filter(id=i)
                elif game.player_2.userPlayer.user.id == request.user.id:
                    sel_card = game.player_2.userHand.filter(id=i)
                # sel_crd = game.player_2.userHand.filter(id=i)
                other_card = Card.objects.get(id=i)
                for e in missing_card:
                    # print(e.stickValue)

                    if game.player_1.userPlayer.user.id == request.user.id:
                        # game.player_1.userHand.remove(e)

                        game.player_1.sticks += e.cardValue

                        game.player_1.save()

                    elif game.player_2.userPlayer.user.id == request.user.id:
                        # game.player_2.userHand.remove(e)

                        game.player_2.sticks += e.stickValue

                        game.player_2.save()

        update_player(game)

        try:
            print("Yoo")
        except:
            print('no good')

        return HttpResponse(
            print("blah")
            )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
            )

@csrf_exempt
def buy_cards(request, game_id):
    """Updates userHand and stick"""
    post_forest = request.POST.getlist('forest[]')
    post_method = request.POST.getlist('method[]')

    if len(post_method) >= 1:
        game = Game.objects.get(id=game_id)
        forest_obj = game.forest_id
        fore = Forest.objects.get(id=forest_obj.id)
        forest = game.forest_id.forestCard.all()
        forest_cards = []
        num = len(post_forest) - 1
        deck = game.deck_id
        forest_num = len(post_forest)

        for i in forest:
            forest_cards.append(i.id)

        card_thats_missing = [str(i) for i in forest_cards]

        missing_card = list(set(card_thats_missing) - set(post_forest))

        card_thats_missing.sort()
        post_forest.sort()

        if forest_num != len(forest_cards):
            for i in missing_card:
                forest_delcard = game.forest_id.forestCard.filter(id=i)
                other_card = Card.objects.get(id=i)
                for e in forest_delcard:

                    if game.player_1.userPlayer.user.id == request.user.id:
                        fu = Player.objects.get(id=game.player_1.id)
                        fu.userHand.add(other_card)
                        fu.sticks -= e.stickValue
                        fu.save()
                    elif game.player_2.userPlayer.user.id == request.user.id:
                        meanie = Player.objects.get(id=game.player_2.id)
                        meanie.userHand.add(other_card)
                        meanie.sticks -= e.stickValue
                        meanie.save()
                    fore.forestCard.remove(e)
                    fore.save()

                while num <= 8:
                    fore.forestCard.add(deck.deckCard.order_by('?').first())
                    fore.save()
                    num += 1

        update_player(game)

        try:
            print("Yoo")
        except:
            print('no good')

        return HttpResponse(
            print("blah")
            )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
            )

def update_player(game):
    """Updates player"""
    if game.current_player == game.player_1:
        # print(game.current_player)
        # print(game.current_player.turns)
        game.current_player = game.player_2
        game.player_1.turns -= 1
        game.player_1.save()
        game.save()
    elif game.current_player == game.player_2:
        print(game.current_player)
        print(game.current_player.turns)
        game.current_player = game.player_1
        game.player_2.turns -= 1
        game.player_2.save()
        game.save()