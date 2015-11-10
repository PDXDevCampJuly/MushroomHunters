# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0003_player_userplayingcards'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='score',
            field=models.IntegerField(default=0, max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='sticks',
            field=models.IntegerField(default=0, max_length=500, null=True, blank=True),
        ),
    ]
