# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0016_auto_20151014_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='deckCard',
            field=models.ManyToManyField(to='Game.Card', related_name='+'),
        ),
    ]
