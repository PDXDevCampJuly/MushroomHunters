# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='location',
        ),
        migrations.AlterField(
            model_name='player',
            name='score',
            field=models.IntegerField(),
        ),
    ]
