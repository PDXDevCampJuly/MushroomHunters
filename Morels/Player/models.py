from django.db import models
# from django_extensions.db.models import (TitleSlugDescriptionModel, TimeStampedModel)

# Create your models here.

class Player(models.Model):
    score = models.IntegerField(max_length=100)

    userHand = models.ManyToManyField(Cards)

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    password = models.TextField(max_length=100)
    location = models.TextField(max_length=500)
    profilepic = models.ImageField(upload_to=None, height_field=100, width_field=100, max_length= 100)
    level = models.IntegerField()

    userPlayers = models.ManyToManyField(Player)

class Bot(models.Model):
    name = models.CharField(max_length=50)
    insults = models.ForeignKey(Insults, default='')

    botPlayers = models.ManyToManyField(Player)

class Insults(models.Model):
    insults = models.CharField(max_length=100)

class LeaderBoard(models.Model):
    user_id = models.ForeignKey(User, default='')
    score = models.ForeignKey(Player, default=0)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)

