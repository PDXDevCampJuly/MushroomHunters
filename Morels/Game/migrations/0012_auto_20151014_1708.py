# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0011_auto_20151014_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='Night_id',
        ),
        migrations.RemoveField(
            model_name='game',
            name='decay_id',
        ),
        migrations.RemoveField(
            model_name='game',
            name='forest_id',
        ),
    ]
