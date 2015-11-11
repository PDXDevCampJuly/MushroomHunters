from django.db import models
from django.contrib.auth.models import User

from Game import models as game_models
# Create your models here.


class MyUser(models.Model):
    profilePic = models.ImageField(upload_to='profile_images', blank=True)
    level = models.IntegerField(default=0)

    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username


class Card(models.Model):
    cardValue = models.IntegerField()
    stickValue = models.IntegerField()
    picture = models.ImageField(upload_to=None, blank=False, default="../../static")
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class Player(models.Model):
    score = models.IntegerField(default=0)
    sticks = models.IntegerField(default=0)
    turns = models.IntegerField(default=20)
    userPlayingCards = models.ManyToManyField(Card, blank=True, related_name='playingcards')
    userHand = models.ManyToManyField(Card, blank=True)
    userPlayer = models.ForeignKey(MyUser)

    def __str__(self):
        return self.userPlayer.user.username


class Invite(models.Model):
    invite_sender = models.ForeignKey(MyUser, related_name='sender')
    invite_receiver = models.ForeignKey(MyUser, related_name='receiver')
    time_sent = models.DateTimeField('')
    status_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.status_accepted


class Insult(models.Model):
    insults = models.CharField(max_length=100)

    def __str__(self):
        return self.insults


class Bot(models.Model):
    name = models.CharField(max_length=50)
    insults = models.ForeignKey(Insult, default='')

    botPlayers = models.ManyToManyField(Player)

    def __str__(self):
        return self.name


class LeaderBoard(models.Model):
    user_id = models.ForeignKey(User, default='')
    score = models.ForeignKey(Player, default=0)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.user_id

