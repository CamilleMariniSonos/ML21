# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('motorapp', '0002_auto_20151122_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('raw_data', models.FileField(max_length=200, null=True, upload_to=b'', blank=True)),
                ('description', models.CharField(max_length=300, null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='problem',
            name='raw',
        ),
        migrations.AddField(
            model_name='problem',
            name='dataset',
            field=models.ForeignKey(blank=True, to='motorapp.Dataset', null=True),
        ),
    ]
