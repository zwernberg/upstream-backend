# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20160110_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='catch',
            field=models.ForeignKey(to='api.Catch', related_name='liked_users'),
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set([('user', 'catch')]),
        ),
    ]
