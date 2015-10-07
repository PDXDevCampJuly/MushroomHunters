# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0004_card_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='picture',
            field=models.ImageField(default='', upload_to=None),
        ),
    ]
