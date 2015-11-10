# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0004_auto_20151110_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='sticks',
            field=models.IntegerField(default=0),
        ),
    ]
