# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motorapp', '0004_auto_20151211_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='cost_function',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='description',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='target',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='train_prop',
        ),
    ]
