from django.shortcuts import render
from .models import *
from random import choice
import sys



def make_decks(request, pid):
    card = Card.objects.all()
    deck = []
    type_amount = {
        'Honey fungus': [Card.objects.get(type='Honey fungus'),10],
        'Shiitake': [Card.objects.get(type='Shiitake'),5],
        'Porcini': [Card.objects.get(type='Porcini'),4],
        'Tree ear': [Card.objects.get(type='Tree ear'),8],
        'Hen of the woods': [Card.objects.get(type='Hen of the woods'),5],
        'Chanterelle': [Card.objects.get(type='Chantrelle'),4],
        'Lawyers wig': [Card.objects.get(type='Lawyars wig'),6],
        'Fairys ring': [Card.objects.get(type='Fairys ring'),4],
        'Morels': [Card.objects.get(type='Morels'),3],
        'Pan': [Card.objects.get(type='Pan'),11],
        'Destroying angel': [Card.objects.get(type='Destroying angel'),5],
        'Butter': [Card.objects.get(type='Butter'),3],
        'Moon': [Card.objects.get(type='Moon'),8],
        'Basket': [Card.objects.get(type='Basket'),5],
        'Cider': [Card.objects.get(type='Cider'),3]}

    for x in type_amount:
        deck.append(type_amount[x][0] * type_amount[x][1])

#
#     i=0
#
#     while i < card:
#         if card[i].type == 'Honey Fungus':
#             deck.append(card[i] * 10)
#         if card[i].type == 'Shiitake':
#             deck.append(card[i] * 5)