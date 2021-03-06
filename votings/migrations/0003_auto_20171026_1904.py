# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 19:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('propositions', '0004_auto_20171007_0228'),
        ('parlamentarians', '0004_auto_20171017_2310'),
        ('votings', '0002_auto_20171002_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votings',
            name='candidateId',
        ),
        migrations.AddField(
            model_name='votings',
            name='candidateID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidateID', to='parlamentarians.Parlamentarians'),
        ),
        migrations.AddField(
            model_name='votings',
            name='propositionID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propositionID', to='propositions.Propositions'),
        ),
    ]
