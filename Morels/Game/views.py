from django.shortcuts import render
from .models import *
from random import choice
from Game.models import Card
import sys
import random

def test(request):
    card = Card.objects.get()
    return render(request, 'game.html')

    # print( Card )

def game(request):
    deck = []
    times = [10, 5, 4, 8, 5, 4, 6, 4, 3, 11, 5, 3, 8, 5, 3]

    Honey_Fungus = Card.objects.get(type='Honey Fungus')
    Shiitake = Card.objects.get(type='Shiitake')
    Porcini = Card.objects.get(type='Porcini')
    Tree_Ear = Card.objects.get(type='Tree Ear')
    Hen_of_the_woods = Card.objects.get(type='Hen of the woods')
    Chanterelle = Card.objects.get(type='Chanterelle')
    Lawyer_Wig = Card.objects.get(type="Lawyer's Wig")
    Fairy_Ring = Card.objects.get(type='Fairy Ring')
    Morel = Card.objects.get(type='Morel')
    Pan = Card.objects.get(type='Pan')
    Destroying_Angel = Card.objects.get(type='Destroying Angel')
    Butter = Card.objects.get(type='Butter')
    Moon = Card.objects.get(type='Moon')
    Basket = Card.objects.get(type='Basket')
    Cider = Card.objects.get(type='Cider')


    lis = [
        Honey_Fungus,
        Shiitake,
        Porcini,
        Tree_Ear,
        Hen_of_the_woods,
        Chanterelle,
        Lawyer_Wig,
        Fairy_Ring,
        Morel,
        Pan,
        Destroying_Angel,
        Butter,
        Moon,
        Basket,
        Cider,
    ]
    i = 0
    for x in lis:
        temp = [x] * times[i]
        i += 1
        for y in temp:
            deck.append(y)



    random.shuffle(deck)
    print(deck)
    return render(request, 'game.html')

#
#     i=0
#
#     while i < card:
#         if card[i].type == 'Honey Fungus':
#             deck.append(card[i] * 10)
#         if card[i].type == 'Shiitake':
#             deck.append(card[i] * 5)