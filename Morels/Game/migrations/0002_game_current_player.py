# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0001_initial'),
        ('Game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='current_player',
            field=models.ForeignKey(default=None, to='Player.Player', related_name='current_player'),
        ),
    ]
