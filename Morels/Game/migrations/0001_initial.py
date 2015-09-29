# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('cardValue', models.IntegerField(max_length=6)),
                ('stickValue', models.IntegerField(max_length=16)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FryingPan',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('card_id', models.ForeignKey(to='Game.Card')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date', models.DateTimeField(verbose_name='')),
                ('decayDeckCard', models.ManyToManyField(related_name='+', to='Game.Card')),
                ('deckCard', models.ManyToManyField(related_name='+', to='Game.Card')),
                ('forestCard', models.ManyToManyField(related_name='+', to='Game.Card')),
                ('nightDeckCard', models.ManyToManyField(related_name='+', to='Game.Card')),
                ('player_1', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
                ('player_2', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
                ('winner', models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Playing_Card',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('card_id', models.ForeignKey(to='Game.Card')),
                ('fryingPan_id', models.ForeignKey(to='Game.FryingPan')),
            ],
        ),
    ]
