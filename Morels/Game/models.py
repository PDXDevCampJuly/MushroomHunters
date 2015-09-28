from django.db import models
import datetime

# Create your models here.

class Game(models.Model):
    Winner = models.ForeignKey(User, default=None)
    Date = models.DateTimeField('')
    Player_1 = models.ForeignKey(User)
    Player_2 = models.ForeignKey(User)

    deckCard = models.ManyToManyField(Cards)
    forestCard = models.ManyToManyField(Cards)
    nightDeckCard = models.ManyToManyField(Cards)
    decayDeckCard = models.ManyToManyField(Cards)

class Cards(models.Model):
    cardValue = models.IntegerField(max_length=6)
    stickValue = models.IntegerField(max_length=16)
    game_id = models.ForeignKey(Game)
    type = models.CharField()

class Playing_Cards(models.Model):
    fryingPan_id = models.ForeignKey(FryingPan)
    card_id = models.ForeignKey(Cards)

class FryingPan(models.Model):
    card_id = models.ForeignKey(Cards)

