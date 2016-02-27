# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catches', '0003_catch_height'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catch',
            old_name='height',
            new_name='length',
        ),
    ]
