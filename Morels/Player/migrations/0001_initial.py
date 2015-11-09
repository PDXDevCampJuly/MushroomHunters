# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('cardValue', models.IntegerField()),
                ('stickValue', models.IntegerField()),
                ('picture', models.ImageField(upload_to=None, default='../../static')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Insult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('insults', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('time_sent', models.DateTimeField(verbose_name='')),
                ('status_accepted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='LeaderBoard',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('profilePic', models.ImageField(upload_to='profile_images', blank=True)),
                ('level', models.IntegerField(default=0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('userHand', models.ManyToManyField(to='Player.Card', blank=True)),
                ('userPlayer', models.ForeignKey(to='Player.MyUser')),
            ],
        ),
        migrations.AddField(
            model_name='leaderboard',
            name='score',
            field=models.ForeignKey(to='Player.Player', default=0),
        ),
        migrations.AddField(
            model_name='leaderboard',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=''),
        ),
        migrations.AddField(
            model_name='invite',
            name='invite_receiver',
            field=models.ForeignKey(to='Player.MyUser', related_name='receiver'),
        ),
        migrations.AddField(
            model_name='invite',
            name='invite_sender',
            field=models.ForeignKey(to='Player.MyUser', related_name='sender'),
        ),
        migrations.AddField(
            model_name='bot',
            name='botPlayers',
            field=models.ManyToManyField(to='Player.Player'),
        ),
        migrations.AddField(
            model_name='bot',
            name='insults',
            field=models.ForeignKey(to='Player.Insult', default=''),
        ),
    ]
