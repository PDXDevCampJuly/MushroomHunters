# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0002_player_sticks'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='userPlayingCards',
            field=models.ManyToManyField(related_name='playingcards', to='Player.Card', blank=True),
        ),
    ]
