# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0003_auto_20151016_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='decay_id',
            field=models.ForeignKey(default=None, to='Game.Decay', related_name='decay_id'),
        ),
        migrations.AlterField(
            model_name='game',
            name='deck_id',
            field=models.ForeignKey(default=None, to='Game.Deck', related_name='deck_id'),
        ),
        migrations.AlterField(
            model_name='game',
            name='forest_id',
            field=models.ForeignKey(default=None, to='Game.Forest', related_name='forest_id'),
        ),
        migrations.AlterField(
            model_name='game',
            name='night_id',
            field=models.ForeignKey(default=None, to='Game.Night', related_name='night_id'),
        ),
        migrations.AlterField(
            model_name='game',
            name='player_1',
            field=models.ForeignKey(to='Player.Player', related_name='player_1'),
        ),
        migrations.AlterField(
            model_name='game',
            name='player_2',
            field=models.ForeignKey(to='Player.Player', related_name='player_2'),
        ),
    ]
