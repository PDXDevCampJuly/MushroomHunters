from django.db import models
from Player.models import *
import datetime

# Create your models here.

class Game(models.Model):
    winner = models.ForeignKey(User, default=None)
    date = models.DateTimeField('')
    player_1 = models.ForeignKey(User)
    player_2 = models.ForeignKey(User)

    deckCard = models.ManyToManyField(Cards)
    forestCard = models.ManyToManyField(Cards)
    nightDeckCard = models.ManyToManyField(Cards)
    decayDeckCard = models.ManyToManyField(Cards)

class Cards(models.Model):
    cardValue = models.IntegerField(max_length=6)
    stickValue = models.IntegerField(max_length=16)
    game_id = models.ForeignKey(Game)
    type = models.CharField()

    def __str__(self):
        return self.type

class Playing_Cards(models.Model):
    fryingPan_id = models.ForeignKey(FryingPan)
    card_id = models.ForeignKey(Cards)

    def __str__(self):
        return self.fryingPan_id

class FryingPan(models.Model):
    card_id = models.ForeignKey(Cards)

    def __str__(self):
        return self.card_id