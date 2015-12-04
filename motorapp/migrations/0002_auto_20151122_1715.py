# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('motorapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.FileField(max_length=200, null=True, upload_to=b'', blank=True)),
                ('description', models.CharField(max_length=300, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pb_type', models.CharField(blank=True, max_length=3, null=True, choices=[(b'CLF', b'classification'), (b'REG', b'regression')])),
                ('cost_function', models.CharField(max_length=200, null=True, blank=True)),
                ('raw', models.FileField(max_length=200, null=True, upload_to=b'', blank=True)),
                ('target', models.FileField(max_length=200, null=True, upload_to=b'', blank=True)),
                ('description', models.CharField(max_length=300, null=True, blank=True)),
                ('train_prop', models.IntegerField(default=68, null=True, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='estimator',
            name='data',
            field=models.ForeignKey(blank=True, to='motorapp.Features', null=True),
        ),
        migrations.DeleteModel(
            name='Data',
        ),
        migrations.AddField(
            model_name='features',
            name='problem',
            field=models.ForeignKey(blank=True, to='motorapp.Problem', null=True),
        ),
    ]
