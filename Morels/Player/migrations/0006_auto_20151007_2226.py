# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0005_auto_20151007_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='profilePic',
            field=models.ImageField(upload_to='profile_images', blank=True),
        ),
    ]
