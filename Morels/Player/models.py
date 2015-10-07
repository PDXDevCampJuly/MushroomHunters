from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MyUser(models.Model):
    # location = models.TextField(max_length=500)
    profilePic = models.ImageField(upload_to='profile_images', blank=True)
    level = models.IntegerField(default=0)

    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username

class Player(models.Model):
    score = models.IntegerField()

    userHand = models.ManyToManyField('Game.Card')
    userPlayers = models.ForeignKey(MyUser, default=None)

    def __str__(self):
        return self.score

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

