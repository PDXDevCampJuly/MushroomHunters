# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0002_auto_20151016_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
