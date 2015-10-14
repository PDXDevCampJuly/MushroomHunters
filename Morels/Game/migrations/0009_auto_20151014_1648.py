# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0008_auto_20151014_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='winner',
            field=models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
