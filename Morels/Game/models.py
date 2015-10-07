from django.db import models
from Player.models import *
# import datetime

# Create your models here.


class Card(models.Model):
    cardValue = models.IntegerField()
    stickValue = models.IntegerField()
    picture = models.ImageField(upload_to=None, blank=False, default="../../Static/morel")
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class FryingPan(models.Model):
    card_id = models.ForeignKey(Card)

    def __str__(self):
        return self.card_id


class Game(models.Model):
    winner = models.ForeignKey(User, default=None)
    date = models.DateTimeField('')
    player_1 = models.ForeignKey(User, related_name='+')
    player_2 = models.ForeignKey(User, related_name='+')

    deckCard = models.ForeignKey(Card, related_name='+', default=None)
    forestCard = models.ForeignKey(Card, related_name='+', default=None)
    nightDeckCard = models.ForeignKey(Card, related_name='+', default=None)
    decayDeckCard = models.ForeignKey(Card, related_name='+', default=None)


class PlayingCard(models.Model):
    fryingPan_id = models.ForeignKey(FryingPan)
    card_id = models.ForeignKey(Card)

    def __str__(self):
        return self.fryingPan_id
