# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0017_auto_20151015_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='deckCard',
            field=models.ManyToManyField(related_name='+', default=None, to='Game.Card'),
        ),
    ]
