from django.shortcuts import render
from .models import *
import sys

# Create your views here.

game = Game()

def make_decks(request):
    games = Game.objects.all()

    # Get the cards from the db
    #Loop through the cards in Cards and push them in a deck