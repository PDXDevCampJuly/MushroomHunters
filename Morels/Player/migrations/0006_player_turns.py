# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0005_auto_20151110_0349'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='turns',
            field=models.IntegerField(default=20),
        ),
    ]
