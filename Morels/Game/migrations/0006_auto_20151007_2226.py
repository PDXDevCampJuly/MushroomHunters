# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0005_auto_20151007_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='picture',
            field=models.ImageField(upload_to=None, default='../../static'),
        ),
    ]
