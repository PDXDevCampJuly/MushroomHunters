# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0002_auto_20151002_2147'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Playing_Card',
            new_name='PlayingCard',
        ),
    ]
