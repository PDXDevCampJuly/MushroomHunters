# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Decay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('decayDeckCard', models.ManyToManyField(default=None, to='Player.Card', related_name='decayCards')),
            ],
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('deckCard', models.ManyToManyField(default=None, to='Player.Card', related_name='deckCards')),
            ],
        ),
        migrations.CreateModel(
            name='Forest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('forestCard', models.ManyToManyField(default=None, to='Player.Card', related_name='forestCards')),
            ],
        ),
        migrations.CreateModel(
            name='FryingPan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('card_id', models.ForeignKey(to='Player.Card')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date', models.DateTimeField(editable=False)),
                ('decay_id', models.ForeignKey(to='Game.Decay', related_name='decay_id', default=None)),
                ('deck_id', models.ForeignKey(to='Game.Deck', related_name='deck_id', default=None)),
                ('forest_id', models.ForeignKey(to='Game.Forest', related_name='forest_id', default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Night',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nightDeckCard', models.ManyToManyField(default=None, to='Player.Card', related_name='nightCards')),
            ],
        ),
        migrations.CreateModel(
            name='PlayingCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('card_id', models.ForeignKey(to='Player.Card')),
                ('fryingPan_id', models.ForeignKey(to='Game.FryingPan')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='night_id',
            field=models.ForeignKey(to='Game.Night', related_name='night_id', default=None),
        ),
        migrations.AddField(
            model_name='game',
            name='player_1',
            field=models.ForeignKey(related_name='player_1', to='Player.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='player_2',
            field=models.ForeignKey(related_name='player_2', to='Player.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, to='Player.MyUser', default=None),
        ),
    ]
