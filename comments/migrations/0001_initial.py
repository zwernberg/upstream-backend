# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(max_length=3000)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='commenter')),
                ('target', models.ForeignKey(to='catches.Catch', related_name='comments')),
            ],
        ),
    ]
