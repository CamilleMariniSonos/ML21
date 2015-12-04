# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('train_data', models.FileField(max_length=200, null=True, upload_to=b'', blank=True)),
                ('train_target', models.FileField(max_length=200, null=True, upload_to=b'', blank=True)),
                ('test_data', models.FileField(max_length=200, null=True, upload_to=b'', blank=True)),
                ('test_target', models.FileField(max_length=200, null=True, upload_to=b'', blank=True)),
                ('pb_type', models.CharField(blank=True, max_length=3, null=True, choices=[(b'CLF', b'classification'), (b'REG', b'regression')])),
                ('cost_function', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estimator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, null=True, blank=True)),
                ('dict_param', models.FileField(max_length=200, null=True, upload_to=b'', blank=True)),
                ('dict_score', models.FileField(max_length=200, null=True, upload_to=b'', blank=True)),
                ('data', models.ForeignKey(blank=True, to='motorapp.Data', null=True)),
            ],
        ),
    ]
