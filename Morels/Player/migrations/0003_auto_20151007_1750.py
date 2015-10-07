# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0002_auto_20151002_2147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='userPlayers',
        ),
        migrations.AddField(
            model_name='player',
            name='userPlayers',
            field=models.ForeignKey(to='Player.MyUser', default=None),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='level',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='profilePic',
            field=models.ImageField(upload_to='profile_images', blank=True),
        ),
    ]
