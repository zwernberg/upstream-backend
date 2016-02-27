# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catches', '0002_catch_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='catch',
            name='height',
            field=models.IntegerField(default=0),
        ),
    ]
