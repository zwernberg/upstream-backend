# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20160212_0157'),
        ('api', '0006_auto_20160203_0139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catch',
            name='owner',
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='like',
            name='catch',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.DeleteModel(
            name='Catch',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
