# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20160207_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='target',
            field=models.ForeignKey(to='catches.Catch', related_name='comments'),
        ),
    ]
