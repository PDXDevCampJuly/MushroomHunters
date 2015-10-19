# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0008_auto_20151016_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='userPlayer',
            field=models.ForeignKey(to='Player.MyUser', blank=True, default=''),
        ),
    ]
