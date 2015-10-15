# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0015_auto_20151014_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='Night_id',
            field=models.ForeignKey(related_name='+', to='Game.Night', default=None),
        ),
        migrations.AlterField(
            model_name='game',
            name='decay_id',
            field=models.ForeignKey(related_name='+', to='Game.Decay', default=None),
        ),
        migrations.AlterField(
            model_name='game',
            name='forest_id',
            field=models.ForeignKey(related_name='+', to='Game.Forest', default=None),
        ),
    ]
