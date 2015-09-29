# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Insult',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('insults', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LeaderBoard',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('location', models.TextField(max_length=500)),
                ('profilePic', models.ImageField(width_field=100, upload_to=None, height_field=100)),
                ('level', models.IntegerField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('score', models.IntegerField(max_length=100)),
                ('userHand', models.ManyToManyField(to='Game.Card')),
            ],
        ),
        migrations.AddField(
            model_name='myuser',
            name='userPlayers',
            field=models.ManyToManyField(to='Player.Player'),
        ),
        migrations.AddField(
            model_name='leaderboard',
            name='score',
            field=models.ForeignKey(default=0, to='Player.Player'),
        ),
        migrations.AddField(
            model_name='leaderboard',
            name='user_id',
            field=models.ForeignKey(default='', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bot',
            name='botPlayers',
            field=models.ManyToManyField(to='Player.Player'),
        ),
        migrations.AddField(
            model_name='bot',
            name='insults',
            field=models.ForeignKey(default='', to='Player.Insult'),
        ),
    ]
