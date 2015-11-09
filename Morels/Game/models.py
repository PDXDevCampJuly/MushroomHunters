from django.db import models
from Player.models import MyUser, Card, Player
from django.utils import timezone
# import datetime

# Create your models here.


class Deck(models.Model):
    deckCard = models.ManyToManyField(Card, related_name='deckCards', default=None)


class Decay(models.Model):
    decayDeckCard = models.ManyToManyField(Card, related_name='decayCards', default=None)


class Forest(models.Model):
    forestCard = models.ManyToManyField(Card, related_name='forestCards', default=None)


class Night(models.Model):
    nightDeckCard = models.ManyToManyField(Card, related_name='nightCards', default=None)


class FryingPan(models.Model):
    card_id = models.ForeignKey(Card)

    def __str__(self):
        return self.card_id


class Game(models.Model):
    winner = models.ForeignKey(MyUser, default=None, blank=True, null=True)
    date = models.DateTimeField(editable=False)
    player_1 = models.ForeignKey(Player, related_name='player_1')
    player_2 = models.ForeignKey(Player, related_name='player_2')
    current_player = models.ForeignKey(Player, related_name='current_player', default=None)

    deck_id = models.ForeignKey(Deck, related_name='deck_id', default=None)
    forest_id = models.ForeignKey(Forest, related_name='forest_id', default=None)
    night_id = models.ForeignKey(Night, related_name='night_id', default=None)
    decay_id = models.ForeignKey(Decay, related_name='decay_id', default=None)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date = timezone.now()

        return super(Game, self).save(*args, **kwargs)


class PlayingCard(models.Model):
    fryingPan_id = models.ForeignKey(FryingPan)
    card_id = models.ForeignKey(Card)

    def __str__(self):
        return self.fryingPan_id










