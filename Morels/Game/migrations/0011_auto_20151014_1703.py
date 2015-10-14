# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0010_auto_20151014_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='Night_id',
            field=models.ForeignKey(to='Game.Deck', default=None, related_name='+'),
        ),
        migrations.AddField(
            model_name='game',
            name='decay_id',
            field=models.ForeignKey(to='Game.Deck', default=None, related_name='+'),
        ),
        migrations.AddField(
            model_name='game',
            name='forest_id',
            field=models.ForeignKey(to='Game.Deck', default=None, related_name='+'),
        ),
        migrations.AlterField(
            model_name='game',
            name='deck_id',
            field=models.ForeignKey(to='Game.Deck', default=None, related_name='+'),
        ),
    ]
