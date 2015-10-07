# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0003_auto_20151007_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='profilePic',
            field=models.ImageField(blank=True, upload_to='Static'),
        ),
    ]
