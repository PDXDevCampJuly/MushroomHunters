# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0013_auto_20151014_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='Decay',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('decayDeckCard', models.ManyToManyField(related_name='+', to='Game.Card', default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Forest',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('forestCard', models.ManyToManyField(related_name='+', to='Game.Card', default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Night',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('nightDeckCard', models.ManyToManyField(related_name='+', to='Game.Card', default=None)),
            ],
        ),
        migrations.RemoveField(
            model_name='deck',
            name='decayDeckCard',
        ),
        migrations.RemoveField(
            model_name='deck',
            name='forestCard',
        ),
        migrations.RemoveField(
            model_name='deck',
            name='nightDeckCard',
        ),
    ]
