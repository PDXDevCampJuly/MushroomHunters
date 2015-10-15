# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0006_auto_20151007_2226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('time_sent', models.DateTimeField(verbose_name='')),
                ('status_accepted', models.BooleanField(default=False)),
                ('invite_resever', models.ForeignKey(related_name='+', to='Player.Player')),
                ('invite_sender', models.ForeignKey(related_name='+', to='Player.Player')),
            ],
        ),
    ]
