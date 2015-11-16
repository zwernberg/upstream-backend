# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20151116_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catch',
            name='fishPhoto',
            field=models.ImageField(upload_to='photos/%Y/%m/%d'),
        ),
    ]
