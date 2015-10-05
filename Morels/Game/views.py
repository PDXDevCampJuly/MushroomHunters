from django.shortcuts import render
from .models import *
import sys

# Create your views here.

game = Game()

def signup(request):


    return render(request, 'signup.html')

# def make_decks(request):
#     games = Game.objects.all()
#
#     for i in range():


    # Get the cards from the db
    #Loop through the cards in Cards and push them in a deck