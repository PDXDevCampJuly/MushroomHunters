from django.db import models
from django.contrib.auth.models import User
# import Game
# from django_extensions.db.models import (TitleSlugDescriptionModel, TimeStampedModel)

# Create your models here.

class Player(models.Model):
    score = models.IntegerField(max_length=100)

    userHand = models.ManyToManyField('Game.Card')

    def __str__(self):
        return self.score

class Insult(models.Model):
    insults = models.CharField(max_length=100)

    def __str__(self):
        return self.insults

class MyUser(models.Model):
    location = models.TextField(max_length=500)
    profilePic = models.ImageField(upload_to=None, height_field=100, width_field=100, max_length= 100)
    level = models.IntegerField()

    user = models.OneToOneField(User)
    userPlayers = models.ManyToManyField(Player)

    def __str__(self):
        return self.user

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

