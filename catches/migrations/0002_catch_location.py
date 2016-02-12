# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catch',
            name='location',
            field=models.CharField(max_length=75, default='Hulls Lake'),
            preserve_default=False,
        ),
    ]
