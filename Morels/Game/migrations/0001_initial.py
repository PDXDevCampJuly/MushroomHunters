# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Decay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decayDeckCard', models.ManyToManyField(default=None, related_name='+', to='Player.Card')),
            ],
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deckCard', models.ManyToManyField(default=None, related_name='+', to='Player.Card')),
            ],
        ),
        migrations.CreateModel(
            name='Forest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forestCard', models.ManyToManyField(default=None, related_name='+', to='Player.Card')),
            ],
        ),
        migrations.CreateModel(
            name='FryingPan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.ForeignKey(to='Player.Card')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(editable=False)),
                ('decay_id', models.ForeignKey(default=None, related_name='+', to='Game.Decay')),
                ('deck_id', models.ForeignKey(default=None, related_name='+', to='Game.Deck')),
                ('forest_id', models.ForeignKey(default=None, related_name='+', to='Game.Forest')),
            ],
        ),
        migrations.CreateModel(
            name='Night',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nightDeckCard', models.ManyToManyField(default=None, related_name='+', to='Player.Card')),
            ],
        ),
        migrations.CreateModel(
            name='PlayingCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.ForeignKey(to='Player.Card')),
                ('fryingPan_id', models.ForeignKey(to='Game.FryingPan')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='night_id',
            field=models.ForeignKey(default=None, related_name='+', to='Game.Night'),
        ),
        migrations.AddField(
            model_name='game',
            name='player_1',
            field=models.ForeignKey(to='Player.Player', related_name='+'),
        ),
        migrations.AddField(
            model_name='game',
            name='player_2',
            field=models.ForeignKey(to='Player.Player', related_name='+'),
        ),
        migrations.AddField(
            model_name='game',
            name='winner',
            field=models.ForeignKey(to='Player.MyUser', blank=True, default=None, null=True),
        ),
    ]
