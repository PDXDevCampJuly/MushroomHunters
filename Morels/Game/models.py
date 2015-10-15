from django.db import models
from Player.models import *
from django.utils import timezone
# import datetime

# Create your models here.


class Card(models.Model):
    cardValue = models.IntegerField()
    stickValue = models.IntegerField()
    picture = models.ImageField(upload_to=None, blank=False, default="../../static")
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type

class Deck(models.Model):
    deckCard = models.ManyToManyField(Card, related_name='+', default=None)

class Decay(models.Model):
    decayDeckCard = models.ManyToManyField(Card, related_name='+', default=None)

class Forest(models.Model):
    forestCard = models.ManyToManyField(Card, related_name='+', default=None)

class Night(models.Model):
    nightDeckCard = models.ManyToManyField(Card, related_name='+', default=None)

class FryingPan(models.Model):
    card_id = models.ForeignKey(Card)

    def __str__(self):
        return self.card_id


class Game(models.Model):
    winner = models.ForeignKey(User, default=None, blank=True, null=True)
    date = models.DateTimeField(editable=False)
    player_1 = models.ForeignKey(User, related_name='+')
    player_2 = models.ForeignKey(User, related_name='+')

    deck_id = models.ForeignKey(Deck, related_name='+', default=None)
    forest_id = models.ForeignKey(Forest, related_name='+', default=None)
    night_id = models.ForeignKey(Night, related_name='+', default=None)
    decay_id =models.ForeignKey(Decay, related_name='+', default=None)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date = timezone.now()

        return super(Game, self).save(*args, **kwargs)



class PlayingCard(models.Model):
    fryingPan_id = models.ForeignKey(FryingPan)
    card_id = models.ForeignKey(Card)

    def __str__(self):
        return self.fryingPan_id
