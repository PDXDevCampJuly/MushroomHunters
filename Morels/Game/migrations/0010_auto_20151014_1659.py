# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0009_auto_20151014_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('decayDeckCard', models.ManyToManyField(to='Game.Card', related_name='+', default=None)),
                ('deckCard', models.ManyToManyField(to='Game.Card', related_name='+', default=None)),
                ('forestCard', models.ManyToManyField(to='Game.Card', related_name='+', default=None)),
                ('nightDeckCard', models.ManyToManyField(to='Game.Card', related_name='+', default=None)),
            ],
        ),
        migrations.RemoveField(
            model_name='game',
            name='decayDeckCard',
        ),
        migrations.RemoveField(
            model_name='game',
            name='deckCard',
        ),
        migrations.RemoveField(
            model_name='game',
            name='forestCard',
        ),
        migrations.RemoveField(
            model_name='game',
            name='nightDeckCard',
        ),
        migrations.AlterField(
            model_name='game',
            name='winner',
            field=models.ForeignKey(default=None, blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='game',
            name='deck_id',
            field=models.ForeignKey(to='Game.Deck', default=None),
        ),
    ]
