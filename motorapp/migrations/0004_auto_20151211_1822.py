# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motorapp', '0003_auto_20151122_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='raw_data',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
