# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0002_auto_20151016_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decay',
            name='decayDeckCard',
            field=models.ManyToManyField(related_name='decayCards', to='Player.Card', default=None),
        ),
        migrations.AlterField(
            model_name='deck',
            name='deckCard',
            field=models.ManyToManyField(related_name='deckCards', to='Player.Card', default=None),
        ),
        migrations.AlterField(
            model_name='night',
            name='nightDeckCard',
            field=models.ManyToManyField(related_name='nightCards', to='Player.Card', default=None),
        ),
    ]
