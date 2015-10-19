# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invite',
            name='invite_receiver',
            field=models.ForeignKey(to='Player.MyUser', related_name='receiver'),
        ),
        migrations.AlterField(
            model_name='invite',
            name='invite_sender',
            field=models.ForeignKey(to='Player.MyUser', related_name='sender'),
        ),
    ]
