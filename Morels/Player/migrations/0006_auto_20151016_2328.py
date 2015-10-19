# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0005_auto_20151016_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='userHand',
            field=models.ManyToManyField(to='Player.Card', blank=True),
        ),
    ]
