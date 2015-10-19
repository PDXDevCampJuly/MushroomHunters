# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0003_auto_20151016_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='userHand',
            field=models.ManyToManyField(default=0, to='Player.Card'),
        ),
    ]
