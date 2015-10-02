from django.shortcuts import render
from .models import *
import sys

# Create your views here.

game = Game()

def make_decks(request):
    games = Game.objects.all()