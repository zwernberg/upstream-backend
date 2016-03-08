# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('catches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catch',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, to='taggit.Tag', verbose_name='Tags', help_text='A comma-separated list of tags.', through='taggit.TaggedItem'),
        ),
    ]
