# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='sticks',
            field=models.IntegerField(default=0),
        ),
    ]
