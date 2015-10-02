# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='cardValue',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='card',
            name='stickValue',
            field=models.IntegerField(),
        ),
        migrations.RemoveField(
            model_name='game',
            name='decayDeckCard',
        ),
        migrations.AddField(
            model_name='game',
            name='decayDeckCard',
            field=models.ForeignKey(to='Game.Card', related_name='+', default=None),
        ),
        migrations.RemoveField(
            model_name='game',
            name='deckCard',
        ),
        migrations.AddField(
            model_name='game',
            name='deckCard',
            field=models.ForeignKey(to='Game.Card', related_name='+', default=None),
        ),
        migrations.RemoveField(
            model_name='game',
            name='forestCard',
        ),
        migrations.AddField(
            model_name='game',
            name='forestCard',
            field=models.ForeignKey(to='Game.Card', related_name='+', default=None),
        ),
        migrations.RemoveField(
            model_name='game',
            name='nightDeckCard',
        ),
        migrations.AddField(
            model_name='game',
            name='nightDeckCard',
            field=models.ForeignKey(to='Game.Card', related_name='+', default=None),
        ),
    ]
