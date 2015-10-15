# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0018_auto_20151015_1729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='Night_id',
            new_name='night_id',
        ),
    ]
